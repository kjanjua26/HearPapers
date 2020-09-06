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

## Results
For the initial experimentation, I converted the paper *Stacked Attention Networks for Image Question Answering* from CVPR 2016 to an audiobook.
The PDF link of the paper: <a href="https://arxiv.org/abs/1511.02274">PDF PAPER</a>.
The converted audiobook: <a href="https://soundcloud.com/kamran-janjua-588816855/yang-stacked-attention-networks-audiobook">LISTEN HERE</a>.

## Notes
I used GTTs and therefore the voice is a bit robotic, I plan on using WaveNet in the future and also (smart) inclusion of sentences from the pdf in the audiobook. Currently the only heuristic is if the character length of a sentence is more than 20, we include in the audiobook. The CVPR paper results are good. Equations are a bit tricky, will need to figure that out in the future.
