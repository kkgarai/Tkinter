from tkinter import *
from PIL import ImageTk,Image

root = Tk()
# Width x Height
root.geometry("580x402")
root.minsize(width=300,height=100)
root.maxsize(width=900,height=600)

photo=ImageTk.PhotoImage(Image.open('Images/img1.jpg'))

my_label=Label(image=photo)
my_label.pack()

root.mainloop()
