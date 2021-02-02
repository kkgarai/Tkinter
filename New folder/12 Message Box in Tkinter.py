from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("733x566")
root.title("Pycharm")

def myfunc():
    print("Mai ek bahut hi natkhat aur shaitaan function hoon")

def help():
    print("Let me help you")
    a=tmsg.showinfo('Help',"KKG will help you")

def rate():
    print("Rate us")
    value=tmsg.askquestion('Your Experience',"Was your experience Good?")
    print(value)
    if value=='yes':
        msg='Great!!!'
    else:
        msg="Sorry to hear that"
    tmsg.showinfo("Experience",msg)

def divya():
    ans = tmsg.askretrycancel("Divya se dosti kar lo", "Sorry Divya nahi banegi aapki dost")
    if ans:
        print("Retry karne pe bhi kuch nahi hoga")

    else:
        print("Bahut badiya bhai cancel kar diya warna pitte")

# #Use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_checkbutton(label="Tick")
# m1.add_radiobutton(label='Radio Button')
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label='Help',command=help)
m3.add_command(label="Rate",command=rate)
m3.add_command(label = "Befriend Divya", command=divya)
mainmenu.add_cascade(label='Help',menu=m3)
root.config(menu=mainmenu)

root.mainloop()