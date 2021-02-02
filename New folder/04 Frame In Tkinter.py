from tkinter import *
from PIL import ImageTk,Image

root = Tk()
# Width x Height
root.geometry("700x350")
root.minsize(width=300,height=100)
root.maxsize(width=900,height=600)

f1=Frame(root,bg='yellow',borderwidth=5,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y,padx=30)

f2=Frame(root,bg='red',borderwidth=5)
f2.pack(side=TOP,fill=X)

l=Label(f1,text="Project Tkinter",fg='blue')
l.pack()

l=Label(f2,text="Hello World",bg='green',font='aerial 20 bold')
l.pack()

root.title("MY GUI")


root.mainloop()
