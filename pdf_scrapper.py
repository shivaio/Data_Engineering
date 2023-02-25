import argparse
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def pdf_scrapper(args):

    output_dir = args.output_dir

    for pdf_file in os.listdir(args.input_dir):
        file_name = pdf_file.split(".")[0] + ".txt"
        file_path = args.input_dir + pdf_file

        pages = []
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = open(file_path, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)

        infile.close()
        converter.close()

        text = output.getvalue()

        lines = text.splitlines()
        lines = [line for line in lines if line != ""]

        with open(f"{output_dir}/{file_name}", 'w') as fp:
            for line in lines:
                fp.write(line + "\n")

        output.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, help="Path of input directory")
    parser.add_argument("--output_dir", type=str, help="Path of output directory")
    args = parser.parse_args()
    pdf_scrapper(args)