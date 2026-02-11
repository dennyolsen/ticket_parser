from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pprint import pprint
import os
import sys

tickets_dir =

for file in os.listdir(tickets_dir):
    if file.endswith(".pdf") or file.endswith(".PDF"):
        print(file)