from tkinter import *
from PIL import ImageTk, Image

root = Tk()
# Width x Height
root.geometry("700x350")
root.minsize(width=300, height=100)
root.maxsize(width=900, height=600)

def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")


user = Label(root, text="Username")
password = Label(root, text="Password")

user.grid(row=0, column=0)
password.grid(row=1, column=0)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(root,text='Submit',command=getvals).grid()

root.title("MY GUI")

root.mainloop()
