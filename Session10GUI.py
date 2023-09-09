# menu button , options menu class , progres menu bar , file menu , message box
# color chooser , font chooser , dialog box , canvas , frame , label frame , message box
# radio button , check button , scale , spin box , scroll bar , list box , combo box
# text box , text area , menu bar , menu , menu item , menu separator , menu check button
# menu radio button , menu cascade , menu tear off , menu post , menu unpost , menu delete
# menu entry config , menu entry type , menu entry index , menu entry invoke , menu entry

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time
# from tkinter import messagebox
# from tkinter import colorchooser
# from tkinter import font
# from tkinter import filedialog

m=tk.Tk()
m.title("Kushagra's GUI")
m.geometry("400x400+100+100")

#menu button
# syntax: Menubutton(master,option=value)
# option: activebackground,activeforeground,bg,bd,bitmap,borderwidth,cursor,disabledforeground,font,foreground,height,highlightbackground,highlightcolor,highlightthickness,image,justify,padx,pady,relief,state,text,textvariable,underline,width,wraplength
m.config(bg="yellow")
# def redbg():
#     m.config(bg="red")
# def greenbg():
#     m.config(bg="green")
# def bluebg():
#     m.config(bg="blue")
# def yellowbg():
#     m.config(bg="yellow")
# mb = Menubutton(m,text="Colours",relief=RAISED,background="white")
# mb.menu = Menu(mb)
# mb["menu"]=mb.menu
# mb.menu.add_checkbutton(label="Red",command=redbg)
# mb.menu.add_checkbutton(label="Green",command=greenbg)
# mb.menu.add_checkbutton(label="Blue",command=bluebg)
# mb.menu.add_checkbutton(label="Yellow",command=yellowbg)
# mb.pack()

#options menu class
#syntax: OptionMenu(master,variable,*values)
#option : activebackground,activeforeground,bg,bd,bitmap,borderwidth,cursor,disabledforeground,font,foreground,height,highlightbackground,highlightcolor,highlightthickness,image,justify,padx,pady,relief,state,text,textvariable,underline,width,wraplength
#variable is the variable that holds the current value , values is the list of values that can be selected
# def red():
#     m.config(bg="red")
# def green():
#     m.config(bg="green")
# def blue():
#     m.config(bg="blue")
# def yellow():
#     m.config(bg="yellow")

# variable = StringVar(m)
# variable.set("Select Colour")
# om = OptionMenu(m,variable,"Red","Green","Blue","Yellow")
# om.pack()


# #progres menu bar
# #syntax: Progressbar(master,option=value)
# #option: background,borderwidth,font,foreground,length,orient,relief,troughcolor,variable,value
# def red():
#     m.config(bg="red")
# def green():
#     m.config(bg="green")
# def blue():
#     m.config(bg="blue")
# def yellow():
#     m.config(bg="yellow")
def fun():
    for i in range(5):
        m.update_idletasks()
        pb["value"]+=10
        time.sleep(1)
    pb["value"]=0
pb = Progressbar(m,orient=HORIZONTAL,length=200,mode="indeterminate")
pb.pack()
b=Button(m,text="START",command=fun)
b.pack()

# #file menu
# #syntax: Menu(master,option=value)
# #option: activebackground,activeborderwidth,activeforeground,bg,bd,cursor,disabledforeground,font,foreground,postcommand,relief,selectcolor,tearoff,title,type
def red():
    m.config(bg="red")
def green():
    m.config(bg="green")
def blue():
    m.config(bg="blue")
def yellow():
    m.config(bg="yellow")

menubar = Menu(m)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Red",command=red)
filemenu.add_command(label="Green",command=green)
filemenu.add_command(label="Blue",command=blue)
filemenu.add_command(label="Yellow",command=yellow)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=m.quit)
menubar.add_cascade(label="Colours",menu=filemenu)
m.config(menu=menubar)


m.mainloop()