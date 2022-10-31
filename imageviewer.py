#icon&images
from tkinter import *
from PIL import ImageTk,Image
root= Tk()
root.title('ICONS AND IMAGES')
root.iconbitmap('youtube.ico')
rock_img=ImageTk.PhotoImage(Image.open('rock.png').resize((50,50)))
scissor_img = ImageTk.PhotoImage(Image.open('scissor.png').resize((50,50)))
paper_img = ImageTk.PhotoImage(Image.open('paper.png').resize((50,50)))
list_image=[paper_img,rock_img,scissor_img]

image_display = Label(image=list_image[0])
def prev(index):
	return
def next(index):
	global button_prev
	global button_next
	global image_display
	image_display.grid_forget()
	image_display = Label(image=list_image[index+1])
	image_display.grid(row=0,columnspan=3)
image_display.grid(row=0,columnspan=3)

button_quit = Button(root, text ='EXIT', command=root.quit)
button_next = Button(root, text ='NEXT', command=lambda: next(image.get_index()))
button_prev = Button(root, text ='PREV',)
button_quit.grid(row=2,column=1)
button_next.grid(row=2,column=2)
button_prev.grid(row=2,column=0)

root.mainloop()
