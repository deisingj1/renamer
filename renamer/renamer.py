import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Listbox
from tkinter import *

from os import listdir
from os.path import isfile, join, normpath

def nothing():
    print("Nothing happened")



mw = tk.Tk()
listbox = tk.Listbox(mw)

def pick_file():
    mw.curr_dir = filedialog.askopenfilenames()
    mw.curr_dir = list(mw.curr_dir)
    for file in mw.curr_dir:
        listbox.insert(END,normpath(file))

def pick_directory():
    mw.curr_dir = filedialog.askdirectory()
    print(mw.curr_dir)
    for file in listdir(mw.curr_dir):
        fullpath = normpath(join(mw.curr_dir, file))
        if(isfile(fullpath)):
            listbox.insert(END,fullpath)

def set_curr_dir(self):
    self.config(text=mw.curr_dir)

def show_about():
    tk.messagebox.showinfo("About","Created by Jesse Deisinger 2019\nReleased under MIT License")

menubar = tk.Menu(mw)

file_menu = tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="Open...", command=pick_file)
file_menu.add_command(label="Open dir...", command=pick_directory)

file_menu.add_command(label="Quit",command=mw.destroy)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_command(label="About", command=show_about)

b_first = tk.Button(mw,text='First')
b_up = tk.Button(mw,text='Up')
b_down = tk.Button(mw,text='Down')
b_last = tk.Button(mw,text='Last')

b_first.grid(column=1,row=0,sticky=(tk.N + tk.S + tk.E + tk.W))
b_up.grid(column=1,row=1,sticky=(tk.N + tk.S + tk.E + tk.W))
b_down.grid(column=1,row=2,sticky=(tk.N + tk.S + tk.E + tk.W))
b_last.grid(column=1,row=3,sticky=(tk.N + tk.S + tk.E + tk.W))

listbox.grid(column=0,row=0,rowspan=4,sticky=(tk.N + tk.S + tk.E + tk.W))

mw.columnconfigure(0,weight=1)
mw.rowconfigure(0,weight=1)
mw.rowconfigure(1,weight=1)
mw.rowconfigure(2,weight=1)
mw.rowconfigure(3,weight=1)
mw.title('Renamer')
mw.config(menu=menubar)

mw.mainloop()
