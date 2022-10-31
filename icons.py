#icon&images
from tkinter import *
from PIL import ImageTk,Image
root= Tk()
root.title('ICONS AND IMAGES')
root.iconbitmap('youtube.ico')

my_img = ImageTk.PhotoImage(Image.open('youtube.png'))
my_label = Label(image=my_img)
my_label.pack()












button_quit = Button(root, text ='EXIT', command=root.quit)
button_quit.pack()

root.mainloop()
