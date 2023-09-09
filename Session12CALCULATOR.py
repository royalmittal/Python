# GUI CALCULATOR

import math
import random
import tkinter as tk
from tkinter import *
from turtle import clear
root=Tk()
root.title("Calculator")
root.geometry("832x800")
root.configure(bg="yellow")
root.resizable(0,0)

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    e3.insert(0,c)
    
def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    e3.insert(0,c)

def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    e3.insert(0,c)

def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    e3.insert(0,c)

def percentage():
    a=int(e1.get())
    b=int(e2.get())
    c=a%b
    e3.insert(0,c)

def power():
    a=int(e1.get())
    b=int(e2.get())
    c=a**b
    e3.insert(0,c)

def floor():
    a=int(e1.get())
    b=int(e2.get())
    c=a//b
    e3.insert(0,c)

def sqrt():
    a=int(e1.get())
    b=int(e2.get())
    c=a**0.5
    e3.insert(0,c)


def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

Button(root,text='Scientific',width=10,height=1,font=("Times New Roman",15,"bold"),command=clear,bd=3,fg="white",bg="blue").place(x=0,y=0)
Button(root,text='Standard',width=10,height=1,font=("Times New Roman",15,"bold"),command=clear,bd=3,fg="white",bg="blue").place(x=150,y=0)
Button(root,text='Unit Conversion',width=15,height=1,font=("Times New Roman",15,"bold"),command=clear,bd=3,fg="white",bg="blue").place(x=300,y=0)
Button(root,text='Currency',width=10,height=1,font=("Times New Roman",15,"bold"),command=clear,bd=3,fg="white",bg="blue").place(x=520,y=0)
Button(root,text='Exit',width=10,height=1,font=("Times New Roman",15,"bold"),command=clear,bd=3,fg="white",bg="blue").place(x=670,y=0)


result = Label(root,background="white",width=103,height=3,borderwidth=3,relief="sunken",text=" ").place(x=0,y=60)






root.mainloop()