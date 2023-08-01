import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pick_raffle import select_random_number

root = Tk()
root.geometry("600x400")
frame = tk.Frame(root)
frame.pack()
filename = ''

def raffle():
    cant_winners = var_cant_winners.get()
    print("cant", cant_winners)
    print("file", filename)

def select_file():
    filename = askopenfilename(filetypes=[('CSV','*.csv'),('excel','*.xlsx')], title="Select a file")
    print("filename", filename)
    return filename    

##### body #####
# title of window
root.title("Pick a raffle")
#label title
# LABEL DE INPUT
#label = tk.Label()
var_cant_winners = tk.StringVar()
entry = tk.Entry(root, textvar=var_cant_winners, width=22, relief="flat")
entry.place(x=270, y=190)

# ingrese archivo
button_file = tk.Button(root, text="Choose a file", cursor="hand2", command=select_file)
button_file.place(x=270, y=220)
# boton de sortear
button_raffle = tk.Button(root, text="Raffle", cursor="hand2", command=raffle)
button_raffle.place(x=290, y=350)
frame.mainloop()
