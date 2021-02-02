from tkinter import *
from PIL import ImageTk,Image

root = Tk()
# Width x Height
root.geometry("700x350")
root.minsize(width=300,height=100)
root.maxsize(width=900,height=600)

root.title("MY GUI")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
title_label=Label(text='The Label widget is a standard Tkinter widget \n'
                       'used to display a text or image on the screen. \n  '
                       'There are a lot of attributes of Label widget. ',
                  bg='red',fg='white',padx=50,pady=30,
                  font=('aerial 18 bold italic'),borderwidth=5,
                  relief=GROOVE)
#title_label.pack()

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

title_label.pack(anchor='n',side=BOTTOM,fill=X,padx=35,pady=20)

'''
photo=ImageTk.PhotoImage(Image.open('Images/img1.jpg'))
my_label=Label(image=photo)
my_label.pack()
'''

root.mainloop()
