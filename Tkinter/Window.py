from tkinter import *

top=Toplevel()
top.geometry("120x100")
top.title("Front")

root=Tk()
root.geometry("280x200")
root.title("Back")

btn=Button(text="New Window",command=top)

mainloop()