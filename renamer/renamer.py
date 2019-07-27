import tkinter as tk

mw = tk.Tk()
mw.title('Renamer')

button1 = tk.Button(mw,text='Hello',width=20,command=mw.destroy)
button1.pack()

mw.mainloop()
