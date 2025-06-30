from pdfminer.high_level import extract_text
import re

text = extract_text("ticket.pdf")

def get_citation():

    start_index = text.find('Citation#')
    end_index = text.find('\n',start_index)
    start_string = text[start_index:end_index]
    citation_string = start_string.split("# ")
    citation = citation_string[1]

    return citation

def get_lastname():
    
    start_index = text.find('(Last)\n')
    end_index = text.find('\nAddress', start_index)
    start_string = text[start_index:end_index]
    lastname_string = start_string.split("(Last)\n\n")
    lastname = lastname_string[1]

    return lastname

def get_firstname():
    
    start_index = text.find('(First)\n\n')
    end_index = text.find('\n\nCity', start_index)
    start_string = text[start_index:end_index]
    firstname_string = start_string.split("\n\n")
    firstname = firstname_string[1]

    return firstname

def get_DOB():
    
    start_index = text.find('DOB\n\n')
    end_index = text.find('\n\nState/Zip', start_index)
    start_string = text[start_index:end_index]
    DOB_string = start_string.split("\n")
    DOB = DOB_string[1] # This is wrong

    return DOB

print("Citation: " + str(get_citation()))
print("Last Name: " + str(get_lastname()))
print("First Name: " + str(get_firstname()))
print("DOB: " + str(get_DOB()))



