# TOWN OF NEDERLAND TICKET PARSER
# Copyright (c) 2025 Dennis Olsen, Grace Gude
# License: MIT

from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
files = ["modified.pdf", "modified1.pdf"]

lastname = ""
firstname = ""
citation = ""
dob = ""
address = ""
city = ""
state = ""
zip = ""
dl = ""
dlState = ""
phone = ""
location = ""
date = ""
statute = ""
description = ""
ethnicity = ""
cdl = False

for file in files:
    fp = open(file, 'rb')
    pages = PDFPage.get_pages(fp)
    for page in pages:
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                if x == 7.0 and y == 719.3687000000001:
                    lastname = text.split('\n')[0]
                    continue
                if x == 97.0 and y == 719.3687000000001:
                    firstname = text.split('\n')[0]
                    continue
                if x == 157.0 and y == 752.2617000000001:
                    citation = str.strip(text.split('Citation# ')[1])
                    continue
                if x == 245.0 and y == 727.4757000000001:
                    dob = text.split('\n')[1]
                    continue
                if x == 6.0 and y == 703.3687000000001:
                    address = text.split('\n')[0]
                    continue
                if x == 162.0 and y == 710.4757000000001:
                    city = text.split('\n')[1]
                    continue
                if x == 240.0 and y == 710.4757000000001:
                    fields = text.split('\n')[1]
                    state = fields.split('/')[0]
                    zip = fields.split('/')[1]
                    continue
                if x == 162.0 and y == 710.4757000000001:
                    city = text.split('\n')[1]
                    continue
                if x == 6.0 and y == 678.4757000000001:
                    dl = text.split('\n')[1]
                    continue
                if x == 94.0 and y == 678.4757000000001:
                    dlState = text.split('\n')[1].split(' ')[0]
                    continue
                if x == 248.0 and y == 678.4757000000001:
                    phone = text.split('\n')[1]
                    continue
                if x == 5.0 and y == 490.36870000000005:
                    location = str.lstrip(text).replace('\n', '')
                    continue
                if x == 5.0 and y == 480.2617:
                    date = text.split(": ")[1].split(" ")[0]
                    continue
                if x == 87.0 and y == 468.4757:
                    statute = text.split('\n')[1]
                    continue
                if x == 9.0 and y == 468.4757:
                    description = text.split('Description\n')[1].split("\n")[0]
                    continue
                if x == 326.0 and y == 753.2617000000001:
                    ethnicity = text.split("\n")[0]
                    continue
                if x == 319.0 and y == 744.2617000000001:
                    if text.split("\n")[2].split(": ")[1] == "Yes":
                        cdl = True
                    continue

    print("Last Name: " + lastname)
    print("First Name: " + firstname)
    print("Citation#: " + citation)
    print("DOB: " + dob)
    print("Address: " + address)
    print("City: " + city)
    print("State: " + state)
    print("Zip Code: " + zip)
    print("DL#: " + dl)
    print("DL State: " + dlState)
    print("Phone#: " + phone)
    print("Location: " + location)
    print("Date: " + date)
    print("Statute: " + statute)
    print("Description: " + description)
    print("Ethnicity: " + ethnicity)
    print("CDL: " + str(cdl))
    print("\n")