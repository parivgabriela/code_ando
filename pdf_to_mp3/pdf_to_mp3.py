# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def user_pick_a_file_view():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filelocation = askopenfilename(
        filetypes=[('PDF','*.pdf')], title="Select a pdf file") # open the dialog GUI
    return filelocation


def read_file_to_audio(filelocation, page=None):
    path = open(filelocation, 'rb')

    # creating a PdfFileReader object
    pdfReader = PyPDF2.PdfReader(path)

    num_pages = len(pdfReader.pages)
    if page == None:
        for p in range(num_pages):
            page = pdfReader.pages[p]
            text = page.extract_text()
    else:
        from_page = pdfReader.pages[0]
        # extracting the text from the PDF
        text = from_page.extract_text()
    # reading the text
    speak = pyttsx3.init()
    print("reading pdf...")
    speak.say(text)
    speak.runAndWait()
    print("Done")

    # the page with which you want to start
    # this will read the page of 25th page.
    
def main():
    filelocation = user_pick_a_file_view() 

    if not filelocation:
        print("you must pick one pdf")
        exit()
    read_file_to_audio(filelocation)

main()