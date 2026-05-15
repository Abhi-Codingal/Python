from tkinter import *
root=Tk()
root.title("Login Screen")
root.geometry("400x400")

frame=Frame(master=root, width=350, height=200, bg="#d0efff")

lbl1=Label(frame, text="Enter Password", bg="#5895D3",fg='white', width=12)

pass_entry=Entry(frame, show="*")

textbox=Text(bg="#BEBEBE",fg="black")

def display():
    password=pass_entry.get()
    message="Congrats, on your new password \n"
    textbox.insert(END,password + "\n")
    textbox.insert(END,message)
    if len(password) > 8:
        textbox.insert(END, "This is a strong password!")
    else:
        textbox.insert(END, "This is not a strong password! Try again")

btn=Button(text="Create Account", command=display, fg='red')

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
pass_entry.place(x=150,y=20)
btn.place(x=130,y=210)
textbox.place(y=250)

root.mainloop()