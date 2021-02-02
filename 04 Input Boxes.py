from tkinter import *

root = Tk()

e=Entry(root,width=40,bg='yellow',fg='red',borderwidth=5)
e.pack()
e.insert(0,"HELLO ")

def myClick():
    mylabel=Label(root,text=e.get())
    mylabel.pack()

myButton=Button(root,text="Enter your Name",command=myClick)
myButton.pack()
#myButton.grid(row=3,column=10)

root.mainloop()