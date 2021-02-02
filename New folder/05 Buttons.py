from tkinter import *
from PIL import ImageTk,Image

root = Tk()
# Width x Height
root.geometry("700x350")
root.minsize(width=300,height=100)
root.maxsize(width=900,height=600)

frame=Frame(root,bg='yellow',borderwidth=5,relief=SUNKEN)
frame.pack(side=LEFT,anchor=NW)

def hello():
    print("Hello Tkinter Buttons")

b1=Button(frame,fg='red',text='Print Now',command=hello)
b1.pack(side=TOP,padx=10,pady=20)

b2 = Button(frame, fg='red', text='Print Now',command=hello)
b2.pack(side=TOP, padx=10, pady=20)

b3 = Button(frame, fg='red', text='Print Now',command=hello)
b3.pack(side=TOP, padx=10, pady=20)

b4 = Button(frame, fg='red', text='Print Now',command=hello)
b4.pack(side=TOP, padx=10, pady=20)

root.title("MY GUI")


root.mainloop()
