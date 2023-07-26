# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filelocation = askopenfilename(
    filetypes=[('PDF','*.pdf')],defaultextension='demo-v1.pdf', title="Select a pdf file") # open the dialog GUI
print(filelocation)

if not filelocation:
    print("you must pick one pdf")
    exit()

path = open(filelocation, 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)

#num_pages = reader.numPagesfor p in range(num_pages):
#    page = reader.getPage(p)
#    text = page.extractText()

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.pages[0]

# extracting the text from the PDF
text = from_page.extract_text()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
