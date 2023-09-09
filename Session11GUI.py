# scroll bar , text , panned wndow , notebook , labelframe , tkMessageBox , colorchooser , font , filedialog , messagebox , ttk
#front end design 
#tkinter is a module in python which is used to design front end of any application
#tkinter is a module which is used to design front end of any application

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time

m=tk.Tk()
m.title("Kushagra's GUI")
m.geometry("400x400+100+100")

# SCROLLBAR
# sb = Scrollbar(m)
# sb.pack(side=RIGHT, fill=Y)
# mylist=Listbox(m, yscrollcommand=sb.set)
# for line in range(100):
#     mylist.insert(END, "This is line number " + str(line))
# mylist.pack(side=LEFT, fill=BOTH)
# sb.config(command=mylist.yview)

# TEXT
# t=Text(m,height=10,width=100)
# t.pack()

# PANED WINDOW
# pw=PanedWindow(m,orient=VERTICAL)
# button=Button(pw,text="Button")
# button.pack(side=TOP)
# button2=Button(pw,text="Button2")
# button2.pack(side=BOTTOM)
# pw.add(button)
# pw.add(button2)
# pw.pack()
#pw.pack(fill=BOTH,expand=True)


# NOTEBOOK
n=Notebook(m)
f1=Frame(n)
f2=Frame(n)

tab1=n.add(f1,text="First")
tab2=n.add(f2,text="Second")
n.pack(fill=BOTH,expand=True)

# LABELFRAME
lf=LabelFrame(m,text="This is a label frame")
lf.pack(fill="both",expand="yes")
left=Label(lf,text="Inside the label frame")
left.pack()

# tkMessageBox

m.mainloop()