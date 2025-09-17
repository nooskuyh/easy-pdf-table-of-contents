import sys
import ast
from pathlib import Path
from typing import List, Any, Optional

# The pikepdf library is the key change here
import pikepdf
from pikepdf import OutlineItem

# --- This function is the same as before ---
def load_bookmarks_from_file(file_path: Path) -> List[Any]:
    """Securely loads and parses a Python list literal from a text file."""
    file_content = file_path.read_text(encoding="utf-8")
    valid_python_string = file_content.replace('null', 'None')
    data = ast.literal_eval(valid_python_string)
    return data

# --- This is the NEW add_outline function, rewritten for pikepdf ---
def add_outline_pikepdf(
    outline_data: List[Any],
    offset: int,
    parent_item: list,  # In pikepdf, an outline is a list of OutlineItems
) -> None:
    """
    Recursively adds outline items using the pikepdf library.

    Args:
        outline_data: The nested list of bookmark specs.
        offset: The page number offset.
        parent_item: The list of sub-outlines to add new items to.
    """
    for chapter_number, title, human_page, subchapters in outline_data:
        # Create the full title, handling cases where chapter_number is None
        if chapter_number is not None:
            full_title = f"{chapter_number} {title}"
        else:
            full_title = title

        # Create a new outline item and append it to the parent's list
        # pikepdf uses 0-based page indices, so we subtract 1
        page_index = human_page - 1 + offset
        new_item = OutlineItem(full_title, page_index)
        parent_item.append(new_item)

        # If there are subchapters, recursively add them to the new item
        if subchapters:
            # The 'subordinate' list of the new item is the parent for the next level
            add_outline_pikepdf(subchapters, offset, new_item.children)

# --- Main execution logic ---
def main():
    if len(sys.argv) != 5:
        print("Usage: python bookmark2.py <in_pdf> <bookmarks_file> <out_pdf> <offset>")
        sys.exit(1)

    in_path = Path(sys.argv[1])
    bookmarks_path = Path(sys.argv[2])
    out_path = Path(sys.argv[3])
    offset = int(sys.argv[4])

    print(f"Processing '{in_path}' with bookmarks from '{bookmarks_path}'...")
    
    # Load the bookmark specification from your text file
    outline_spec = load_bookmarks_from_file(bookmarks_path)

    # 1. Open the PDF with pikepdf
    with pikepdf.Pdf.open(in_path) as pdf:
        # 2. Delete any existing outline to start fresh
        try:
            del pdf.Root.Outlines
        except KeyError:
            # No outline existed, which is fine
            pass

        # 3. Use a context manager to work with the outline
        with pdf.open_outline() as outline:
            # 4. Call our recursive function to build the new outline
            add_outline_pikepdf(outline_spec, offset, outline.root)

        # 5. Save the modified PDF to the output file
        pdf.save(out_path)

    print(f"✓ Successfully added bookmarks → '{out_path}'")

if __name__ == "__main__":
    main()