from tkinter import *
#everything is a wedgit in tkinter
total=0
root = Tk()
root.title("Calculator")

display = Entry(root, width=35, borderwidth=5,bg='white')

def button_click(number):
	current = display.get()
	display.delete(0,END)
	display.insert(0,str(current)+str(number))
def button_plus():
	global f_num
	global choice
	choice='add'
	f_num=float(display.get())
	clear()
def button_minus():
	global f_num
	global choice
	choice='minus'
	f_num=float(display.get())
	clear()
def button_div():
	global f_num
	global choice
	choice='div'
	f_num=float(display.get())
	clear()
def button_x():
	global f_num
	global choice
	choice='x'
	f_num=float(display.get())
	clear()
def button_equal():
	s_num=float(display.get())
	clear()
	if choice=='add':
		total=f_num+s_num
	elif choice =='minus':
		total=f_num-s_num
	elif choice =='x':
		total=f_num*s_num
	elif choice =='div':
		total=f_num/s_num
	display.insert(0,total)
def clear():
	display.delete(0,END)
button_0 = Button(root,text='0',padx=40,pady=20,command=lambda:button_click(0))
button_1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root,text='2',padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root,text='3',padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root,text='4',padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root,text='5',padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root,text='6',padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root,text='7',padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root,text='8',padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root,text='9',padx=40,pady=20,command=lambda: button_click(9))
button_clear= Button(root,text='CLEAR',padx=25,pady=20,command=clear)
button_enter= Button(root,text='ENTER',padx=25,pady=20,command=button_equal)
button_plus=Button(root,text='+',padx=39,pady=20,command=button_plus)
button_period=Button(root,text='.',padx=39,pady=20,command=lambda: button_click('.'))
button_div=Button(root,text='/',padx=42,pady=20,command=button_div)
button_minus=Button(root,text='-',padx=39,pady=20,command=button_minus)
button_x=Button(root,text='X',padx=38,pady=20,command=button_x)
#put buttons on screen
display.grid(row=0,column=0,columnspan=3)
button_clear.grid(row=0,column=3)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_div.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_x.grid(row=2,column=3)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_minus.grid(row=3,column=3)

button_0.grid(row=4,column=0)
button_period.grid(row=4, column=1)
button_enter.grid(row=4,column=2)
button_plus.grid(row=4,column=3)

root.mainloop()