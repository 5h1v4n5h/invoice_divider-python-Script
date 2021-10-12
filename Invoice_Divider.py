from PyPDF2 import PdfFileWriter, PdfFileReader
from pdfminer.high_level import extract_text
import os
'''
This Python file is made to extract individual vouchers from a file having Large
number of voucher and name the file as the name of the buyer of the goods
'''
inputpdf = PdfFileReader(open("Document.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    text = extract_text("Document.pdf",page_numbers=[i])
    start=text.find("Buyer")
    stop=text.find("District")
    invo=text.find("CHSAL")
    invo_text=text[(invo):(invo+33)]
    invo_index=invo_text.find('\n')
    invo_name=invo_text[:invo_index]
    name=text[(start+6):(stop-1)]
    nam=name.find('\n')
    string=name[0:nam]
    directory_path = os.getcwd()
    try:
        os.mkdir(directory_path+'//'+string)
    except:
        print()
    try:
        with open(directory_path+'//'+string+'//'+string+' '+str(invo_name)+'.pdf', "wb") as outputStream:
            output.write(outputStream)
    except:
        raise Exception("Document already exist")


