from tkinter import *
#everything is a wedgit in tkinter
def myClick():
	myLabel = Label(root, text='look it works')
	myLabel.pack()
root = Tk()
#state DISABLED is another parameter as well as padx and pady which take int values, fg sets text color
myButton=Button(root,text='click me!',padx=50,pady=50, fg='red',command=myClick)
myButton.pack()
root.mainloop()