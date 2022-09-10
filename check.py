from tkinter import *

root = Tk()

img = PhotoImage(file='background.png')
lb = Label(root, image=img)

lb.place(x=0, y=0)

root.mainloop()