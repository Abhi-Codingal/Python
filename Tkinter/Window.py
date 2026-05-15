from tkinter import *
root=Tk()
root.geometry("280x200")
root.title("Back")

btn=Button(text="Top",command=top)

top=Toplevel()
top.geometry("120x100")
top.title("Front")

mainloop()