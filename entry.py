from tkinter import *
#everything is a wedgit in tkinter
def myClick():
	hello= "Hello" + e.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()
root = Tk()
e = Entry(root, width=50, fg='blue',borderwidth=5)
e.pack()
e.insert(0,"Enter your name: ")	#inserts text in text box
myButton= Button(root,text='Enter your name',command=myClick)
myButton.pack()

root.mainloop()