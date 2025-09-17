<a id="readme-top"></a>


<!-- ABOUT THE PROJECT -->
## About The Project
We can use LLM for parshing a table of contents and put in a pdf easily.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

```
pip3 install pikepdf
```

### Format
```

"[" name_of_chapter(Nullable) , title, page_number(+/-), sub_chapter(list) "]"

```

If you want to generate a table of contents file automatically. Copy the raw text of the table of contents from pdf. Use this prompt to LLM with a copy text of table of contents. I'll add a llm api for this task later.

```
Format this text as follwing

[ name_of_chapter(Nullable) , title, page_number,

[name_of_chapter, title, page_number, []

(Raw text from the book)
... ]


```


<!-- USAGE EXAMPLES -->
## Usage

```
python main.py <in_pdf> <bookmarks_file> <out_pdf> + <offset=0>
```
