'''
GUI IN PYTHON
GUI: Graphical User Interface
Tkinter: Tool Kit Interface
Tkinter is a preinstalled package in python
Tkinter is a python binding to the Tk GUI toolkit
Tkinter is the standard GUI library for python

Basic Steps to create a GUI
1. Import the Tkinter module
2. Create the GUI application's main window
3. Add one or more widgets to the GUI application
4. Enter the main event loop to take action against each event triggered by the user

import tkinter
m = tkinter.Tk()
m.mainloop()

'''
# window , button , label , checkbutton , radiobutton 


import tkinter as tk
from tkinter import *
from tkinter import messagebox as m_box

# Creating the main window
m = tk.Tk()
# Adding a label to the window
m.title("My First GUI")
# setting the size of the window
m.geometry("500x500+500+00")
# resizing the window
#m.resizable(False, True)
def fun():
    print("Jai Shree Ram")

# button to terminate gui window
# button = tk.Button(m, text="Jai Shree Ram", width=15,bg='red',fg='yellow',activebackground='yellow',activeforeground='red',bd=5,command=fun)
# button.pack(side='bottom0')
# button.place(x=50,y=70)
# button.place(relx=0.5,rely=0.5,anchor=CENTER)
#button.grid(row=0,column=0,padx=10,pady=10)


#label
# syntax:
# label_name = Label(window_name, text="text", bg="color", fg="color", font="font", width="width", height="height")
# label=Label(m,text="Jai Shree Ram",bg='red',fg='yellow',font=('Times New Roman',20,'bold'),width=15,height=5)
# label.pack()


#checkbutton
# syntax:
# checkbutton_name = Checkbutton(window_name, text="text", bg="color", fg="color", font="font", width="width", height="height")
# checkbutton1=Checkbutton(m,text="Jai Shree Ram",bg='red',fg='yellow',font=('Times New Roman',15,'bold'),width=15,height=5)
# checkbutton2=Checkbutton(m,text="Har Har Mahadev",bg='red',fg='yellow',font=('Times New Roman',15,'bold'),width=15,height=5)
# checkbutton3=Checkbutton(m,text="Radhe Radhe",bg='red',fg='yellow',font=('Times New Roman',15,'bold'),width=15,height=5)
# checkbutton1.pack()
# checkbutton2.pack()
# checkbutton3.pack()


#radiobutton
# syntax:
# radiobutton_name = Radiobutton(window_name, text="text", bg="color", fg="color", font="font", width="width", height="height")
radiobutton1=Radiobutton(m,text="Jai Shree Ram",bg='red',fg='yellow',font=('Times New Roman',15,'bold'),width=15,height=5,value=0)
radiobutton2=Radiobutton(m,text="Har Har Mahadev",bg='red',fg='yellow',font=('Times New Roman',15,'bold'),width=15,height=5,value=1)
radiobutton3=Radiobutton(m,text="Radhe Radhe",bg='red',fg='yellow',font=('Times New Roman',15,'bold'),width=15,height=5,value=2)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()


#visibliity of the window
m.mainloop()


