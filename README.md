<a id="readme-top"></a>


<!-- ABOUT THE PROJECT -->
# EasyTOC
Putting a table of contents in a pdf easily.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

```
pip3 install pikepdf
```

### Table of Contents Format
```

"[" name_of_chapter , title, page_number, sub_chapter(list) "]"

```
* number_of_chapter (string/null): The chapter identifier, like "1" or "A.1". If there is none, use an empty string "".
* title (string): The title of the chapter or section.
* page_number (integer): The literal page number as it appears in the table of contents.
* sub_chapters (list): A nested list for any sub-chapters. This must be an empty list [] if there are no sub-chapters. 

To generate this file automatically, copy the raw text of the table of contents from your PDF. Then, use the following prompt with an LLM to format the text correctly. I'll add a llm api for this task later.
```
Format this text as follwing

[ name_of_chapter(nullable) , title, page_number,

[name_of_chapter, title, page_number, [] ... ]

(Paste the raw table of contents text here)
```

<img width="481" height="330" alt="image" src="https://github.com/user-attachments/assets/da0d6e9d-cf85-4da7-9f1e-f1a6a33cd3d5" />


<!-- USAGE EXAMPLES -->
## Usage

```
python main.py input.pdf bookmarks.txt output.pdf (offset)
```
* input.pdf: Path to the source PDF file as "sample.pdf".
* bookmarks.txt: Path to the formatted bookmarks text file as "sample_toc.txt".
* output.pdf: Path for the new PDF file with bookmarks.
* offset: (Optional) A number to add or subtract from all page numbers. For example, if the book's page '1' is the 15th page of the PDF file, you would use --offset 14. Defaults to 0.
