import pyttsx3
import PyPDF2
a = input("Enter File Name :")
book= open(a, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
b = input("Enter Page No. to Start From :")
for num in range(int(b), int(pages)):
    page = pdfReader.getPage(num)
    text =page.extractText()
    speaker.say(text)
    speaker.runAndWait()
