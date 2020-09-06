# HearPapers
HearPapers allows you to listen to PDFs (by converting them to audiobooks, of sorts). You can pass in the PDF and it will allow return a .mp3 file which you can listen to.

The code `convert_to_audiobook.py` allows you to pass in the pdf file path and the path to store the audiobook to and it will save a .mp3 file to the path specified.

Running `python3 convert_to_audiobook.py -h` returns:

```
usage: convert_to_audiobook.py [-h] --paper PAPER --path PATH

optional arguments:
  -h, --help     show this help message and exit
  --paper PAPER  The path of the pdf paper you want to convert to audiobook
  --path PATH    The save path - to save the audiobook
```

Note: This is currently tested only for CVPR papers, I am not sure about others since the text extracting follows the CVPR style guide.
