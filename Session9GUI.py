# entry , background color , top level , scale , spin box , frame 
import random
import tkinter as tk
from tkinter import *
m = tk.Tk()
m.title("Kushagra's GUI")
m.geometry("500x500+100+100")
m.resizable(True,True)

# frame
# it is used to group widgets , it is used to organize widgets
# syntax:
# frame_name = Frame(window_name, bg="color", width="width", height="height")
f1 = Frame(m,bg='red',width=200,height=200)
f1.pack(side='left')
f2 = Frame(m,bg='yellow',width=200,height=200)
f2.pack(side='right')
f3 = Frame(m,bg='blue',width=200,height=200)
f3.pack(side='top')
f4 = Frame(m,bg='green',width=200,height=200)
f4.pack(side='bottom')

# entry
# it is used to take input from the user , it is used to take input from the user in a single line
# syntax:
# entry_name = Entry(window_name, text="text", bg="color", fg="color", font="font", width="width", height="height")
l1 = Label(m,text="Enter your name")
l1.place(x=200,y=25)
e1 = Entry(m,width=25,background='red')
e1.place(x=200,y=50)

l2 = Label(m,text="Enter your age")
l2.place(x=200,y=75)
e2 = Entry(m,width=25,background='yellow')
e2.place(x=200,y=100)

l3 = Label(m,text="Enter your address")
l3.place(x=200,y=125)
e3 = Entry(m,width=25,background='blue')
e3.place(x=200,y=150)

# background color
# it is used to change the background color of the window , it is used to change the background color of the widgets
# syntax:
# window_name.configure(bg="color")

def fun0():
    colors = ['red','green','blue','yellow','pink','orange','purple']
    m.configure(bg=random.choice(colors))

button = Button(m,text="Click To Change Background Color",command=fun0,background='green')
button.place(x=50,y=300)

# top level
# it is used to create a new window , it is used to create a new window on top of the main window
# syntax:
# top_level_name = Toplevel(window_name, bg="color", width="width", height="height") 
l1=Label(m,text="Main Window",font=('Times New Roman',15,'bold'))
l1.pack()
def fun():
    top = Toplevel(m,bg='red',width=200,height=200)
    top.title("Top Level")
    top.geometry("200x200+100+100")
    l2=Label(top,text="Top Level",font=('Times New Roman',15,'bold'))
    l2.pack()
button = Button(m,text="Click To Open Top Level",command=fun)
button.pack()

# scale
# it is used to select from a range of values
# syntax:
# scale_name = Scale(window_name, from_=0, to=100, bg="color", fg="color", font="font", width="width", height="height")
s1 = Scale(m,from_=0,to=100,orient=HORIZONTAL,background='red')
s2 = Scale(m,from_=100,to=100,orient=VERTICAL,background='yellow')
s3 = Scale(m,from_=100,to=200,orient=HORIZONTAL,background='blue')
s1.pack()
s2.pack()
s3.pack()

# spin box
# it is used to select from a fixed set of values
# syntax:
# spin_box_name = Spinbox(window_name, from_=0, to=100, bg="color", fg="color", font="font", width="width", height="height")
sb1 = Spinbox(m,from_=0,to=100,increment=2,background='red')
sb2 = Spinbox(m,from_=100,to=100,background='yellow')
sb3 = Spinbox(m,from_=100,to=200,background='blue')
sb1.pack()
sb2.pack()
sb3.pack()

b1=Button(m,text="Click To Exit",command=m.destroy,background='yellow')
b1.pack(side='bottom')

m.mainloop()