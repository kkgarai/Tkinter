
from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("Title Of My GUI")
root.wm_iconbitmap("C:\\Users\\KIRAN\\Desktop\\KKG\\Tkinter\\icon.ico")
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

def quit():
    root.destroy()

print(f"{width}x{height}")
Button(text="Close", command = quit).pack()

root.mainloop()
