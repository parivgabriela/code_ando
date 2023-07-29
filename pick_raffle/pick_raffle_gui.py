from tkinter import * 
from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry("300x150")
frame = Frame(root)
frame.pack()

def ask_file_view():
    
    w = Label(root, text ='Pick Raffle', font = "50") 
    w.pack()
    
    frame = Frame(root)
    frame.pack()
    
    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )
    root.mainloop()

    filelocation = askopenfilename(
        filetypes=[('PDF','*.pdf')], title="Select a pdf file") # open the dialog GUI
    return filelocation

def demo():
    # example
    w = Label(root, text ='GeeksForGeeks', font = "50") 
    w.pack()
    

    
    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )
    
    b1_button = Button(frame, text ="Geeks1", fg ="red")
    b1_button.pack( side = LEFT)
 
def printInput(inputtxt,lbl):
	inp = inputtxt.get(1.0, "end-1c")
	lbl.config(text = "Provided Input: "+inp)

def view_input():
     # TextBox Creation
    inputtxt = Text(frame,
    				height = 5,
    				width = 20)

    inputtxt.pack()
    lbl = Label(frame, text = "")
    # Button Creation
    printButton = Button(frame,
    						text = "Print",
    						command = printInput(inputtxt,lbl))
    printButton.pack()
    lbl.pack()

    frame.mainloop()






view_input()