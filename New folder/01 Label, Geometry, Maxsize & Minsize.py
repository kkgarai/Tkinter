from tkinter import *

root = Tk()
# Width x Height
root.geometry("700x350")
root.minsize(width=300,height=100)
root.maxsize(width=900,height=600)

my_label=Label(text='This is a GUI')
my_label.pack()

root.mainloop()
