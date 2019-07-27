import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Listbox
from tkinter import *

from os import listdir,rename
from os.path import isfile, join, normpath, dirname

from string import Template

mw = tk.Tk()
listbox = tk.Listbox(mw)
targetbox = tk.Listbox(mw)

rename_path = tk.Entry(mw)
start_number = tk.Entry(mw)
count = 1

# This is super duper not thread safe
def count_postinc():
    global count
    count += 1
    return count - 1

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

def get_rename_path(pathstr):
    return normpath(Template(rename_path.get()).substitute(sdir=dirname(pathstr), cnt=count_postinc()))

def movefirst():
    listbox.insert(0,listbox.get(ACTIVE))
    listbox.delete(ACTIVE)

def moveup():
    if listbox.index(ACTIVE) > 0:
        listbox.insert(listbox.index(ACTIVE)-1,listbox.get(ACTIVE))
        listbox.activate(listbox.index(ACTIVE)-2)
        listbox.delete(listbox.index(ACTIVE)+2)

def movedown():
    if listbox.index(ACTIVE) < listbox.index(END)-1:
        listbox.insert(listbox.index(ACTIVE)+2,listbox.get(ACTIVE))
        listbox.activate(listbox.index(ACTIVE)+2)
        listbox.delete(listbox.index(ACTIVE)-2)

def movelast():
    listbox.insert(END,listbox.get(ACTIVE))
    listbox.delete(ACTIVE)

def deleteitem():
    listbox.delete(ACTIVE)

def show_about():
    tk.messagebox.showinfo("About","Created by Jesse Deisinger 2019\nReleased under MIT License")

def applyrename():
    global count
    if start_number.get():
        count = int(start_number.get())
    else:
        count = 1
    targetbox.delete(0,END)
    for path in listbox.get(0,END):
        targetbox.insert(END,get_rename_path(path))

def rename_files():
    for num,path in enumerate(listbox.get(0,END),start=0):
        print(path + "->" + targetbox.get(num))
        rename(path,targetbox.get(num))

menubar = tk.Menu(mw)

file_menu = tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="Open...", command=pick_file)
file_menu.add_command(label="Open dir...", command=pick_directory)
file_menu.add_command(label="Quit",command=mw.destroy)

edit_menu = tk.Menu(menubar,tearoff=0)
edit_menu.add_command(label="Rename", command=rename_files)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)

menubar.add_command(label="About", command=show_about)

b_first = tk.Button(mw,text='First',command=movefirst)
b_up = tk.Button(mw,text='Up',command=moveup)
b_down = tk.Button(mw,text='Down',command=movedown)
b_last = tk.Button(mw,text='Last',command=movelast)
b_del = tk.Button(mw,text='Delete',command=deleteitem)

b_apply = tk.Button(mw,text='Apply',command=applyrename)

b_first.grid(column=2,row=0,sticky=(tk.N + tk.S + tk.E + tk.W))
b_up.grid(column=2,row=1,sticky=(tk.N + tk.S + tk.E + tk.W))
b_down.grid(column=2,row=2,sticky=(tk.N + tk.S + tk.E + tk.W))
b_last.grid(column=2,row=3,sticky=(tk.N + tk.S + tk.E + tk.W))
b_del.grid(column=2,row=4,sticky=(tk.N + tk.S + tk.E + tk.W))
b_apply.grid(column=2,row=5,sticky=(tk.N + tk.S + tk.E + tk.W))


listbox.grid(column=0,row=0,rowspan=5,sticky=(tk.N + tk.S + tk.E + tk.W))
targetbox.grid(column=1,row=0,rowspan=5,sticky=(tk.N + tk.S + tk.E + tk.W))

rename_path.grid(column=0,row=5, columnspan=2, sticky=(tk.E+tk.W))
start_number.grid(column=0,row=6)

mw.columnconfigure(0,weight=1)
mw.columnconfigure(1,weight=1)

mw.rowconfigure(0,weight=1)
mw.rowconfigure(1,weight=1)
mw.rowconfigure(2,weight=1)
mw.rowconfigure(3,weight=1)
mw.rowconfigure(4,weight=2)
mw.rowconfigure(5,weight=1)

mw.title('Renamer')
mw.config(menu=menubar)

mw.mainloop()
