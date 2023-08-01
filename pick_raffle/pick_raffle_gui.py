import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pick_raffle import select_winners_from_file
from tkinter.messagebox import showinfo
from validators import validate_number_input

root = Tk()
root.geometry("600x320")
frame = tk.Frame(root)
root.resizable(False, False)
frame.pack()
filename = ''
gui_title = "Pick a raffle"

def close_window():
    root.destroy()

def show_winners(list_winners):
    root.withdraw()
    window_winner = tk.Toplevel()
    window_winner.geometry("600x400")
    window_winner.title(gui_title)
    window_winner.resizable(False, False)

    def return_main_window():
        window_winner.withdraw()
        root.deiconify()

    button_return_root_window = tk.Button(window_winner, text="Return", cursor="hand2", command=return_main_window)
    button_return_root_window.place(x=230, y=280)
    button_close_window = tk.Button(window_winner, text="Close", cursor="hand2", command=close_window)
    button_close_window.place(x=310, y=280)

    position_y = 20
    for index, winner in enumerate(list_winners, start=1):
        #name_label = f"label_winner{index}"
        position_y = position_y + 30
        text_label = f"{index} place {winner}"
        name_label = tk.Label(window_winner, text = text_label).place(x=220, y=position_y)
    
    window_winner.mainloop()


def raffle():
    """button triger the raffle
    """
    try:
        cant_winners = var_cant_winners.get() # todo validate only numbers and must be less than the len of file
        message = validate_number_input(cant_winners)
        if not message:
            filename = in_filename.get()
            list_winners = select_winners_from_file(filename, cant_winners)
            show_winners(list_winners)
        else:
            showinfo(title="retry", message=message)
    except:
        showinfo(title="retry", message="Enter a valid number")
    

def select_file():
    """button trigger pick a file
    """
    path_filename = askopenfilename(filetypes=[('CSV','*.csv'),('excel','*.xlsx')], title="Select a file")
    filename = path_filename
    print("filename", filename)
    entry_filename.config(state='normal')
    entry_filename.delete(0, tk.END)
    entry_filename.insert(0,filename)
    entry_filename.config(state='readonly')

    showinfo(title='Selected File', message=filename)

##### body #####
# title of window
root.title(gui_title)
#label title
l_body = tk.Label(root, text = "Welcome to Pick Raffle").place(x = 220, y = 20) 

# LABEL DE INPUT
l_enter_winners = tk.Label(root, text = "Enter number of winners").place(x = 100, y = 90) 

var_cant_winners = tk.StringVar()
entry_cant_winner = tk.Entry(root, textvar=var_cant_winners, width=22, relief="flat")
entry_cant_winner.place(x=300, y=90)

# ingrese archivo
#label
l_choose_a_file = tk.Label(root, text = "Choose a file").place(x = 100, y = 140) 
in_filename = tk.StringVar()
entry_filename = tk.Entry(root, textvar=in_filename, width=22, relief="flat", state='disabled')
entry_filename.place(x=300, y=180)
   
#button to get the file
button_file = tk.Button(root, text="Files", cursor="hand2", command=select_file)
button_file.place(x=300, y=140)
# boton de sortear
button_raffle = tk.Button(root, text="Raffle", cursor="hand2", command=raffle)
button_raffle.place(x=280, y=270)

frame.mainloop()
