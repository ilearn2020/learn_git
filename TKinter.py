
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


def say_hello():
    messagebox.showinfo('Greetings', 'hello')

def say_bonjour():
    messagebox.showinfo('Greetings', 'bonjour')

def say_au_revoir():
    messagebox.showinfo('Greetings', 'au revoir')



root_window =Tk()

root_window.title('First_Program')

label_1 = Label(root_window, text="I am in the root window")
label_1.pack()

hello_frame = Frame(root_window)
hello_frame.pack()

hello_label = Label(hello_frame, text = 'I am in the hello frame')
hello_button = Button(hello_frame, text = 'Say hello', command=say_hello)

hello_label.grid(row=0, column=0, pady=2)
hello_button.grid(row=0, column=1, pady=0)

french_frame = Frame(root_window)
french_frame.pack()


bonjour_frame = Frame(french_frame)
au_revoir_frame = Frame(french_frame)

bonjour_button = Button(bonjour_frame, text = 'Say bonjour', command=say_bonjour)
bonjour_button.pack()
au_revoir_button = Button(au_revoir_frame, text = 'Say au revoir', command=say_au_revoir)
au_revoir_button.pack()

bonjour_frame.grid(row=0, column=0, pady=2)
au_revoir_frame.grid(row=0,column=1,pady=2)


root_window.mainloop()
