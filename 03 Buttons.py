from tkinter import *

root = Tk()

def myClick():
    mylabel=Label(root,text="Clicked !!!")
    mylabel.pack()

myButton=Button(root,text="Click Me",padx=30,pady=10,command=myClick,fg='blue',bg='red')
myButton.pack()
#myButton.grid(row=3,column=10)

root.mainloop()