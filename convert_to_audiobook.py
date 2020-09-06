"""
Convert the paper to audiobook and listen to it.
"""

import argparse
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from gtts import gTTS

# command line arguments
args_parser = argparse.ArgumentParser()
args_parser.add_argument('--paper', help='The path of the pdf paper you want to convert to audiobook', action='store', type=str, required=True)
args_parser.add_argument('--path', help='The save path - to save the audiobook', action='store', type=str, required=True)
args = args_parser.parse_args()

paper = args.paper
download_path = args.path

class AudioBook:
    def convert_to_text(self, pdf_path):
        """
        Converts the PDF to text for reading.
        Function taken from: 
            https://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python/26495057
        """

        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        fp = open(pdf_path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()
        return text
    
    def to_audiobook(self):
        """
        Converts the paper to audiobook.
        """
        paper_body = []
        
        text_of_the_paper = self.convert_to_text(paper)
        pre_abs, post_abs = text_of_the_paper.split('Abstract')
        pre_refs, post_refs = post_abs.split('References')
        # only use post-abstract and pre-references text.

        for ix, line in enumerate(pre_refs.split('\n')):
            if len(line) > 20:
                # follows an assumption that line length over 20 is paper content.
                paper_body.append(line)

        body = ' '.join([x for x in paper_body])
        body = body.replace('- ', '')
        speech = gTTS(text = body, lang = "en", slow = False)
        speech.save(download_path + "/paper_audio.mp3")
        print("Audiobook saved to {}".format(download_path))

to_audio = AudioBook()
to_audio.to_audiobook()