from tkinter import *

def func(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

def quit(event):
    root.destroy()

root=Tk()
root.title("Events in Tkinter")
root.geometry('700x400')

widget=Button(root,text='CLick me please')
widget.pack()


widget.bind('<Button-1>',func)
widget.bind('<Double-1>', quit)

root.mainloop()