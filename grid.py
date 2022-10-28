from tkinter import *
#everything is a wedgit in tkinter

root = Tk()

#grid places the elements by row and index and is relative

#create label wedgit can also slap grid object on end it on the end and it works too
myLabel = Label(root,text="hello world!").grid(row=0,column=0)
myLabel2 = Label(root,text="my name is kobe fujimoto").grid(row=1,column=5)

#opens this loop/closing window breaks this loop
root.mainloop()