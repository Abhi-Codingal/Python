from tkinter import *
import math
root=Tk()
root.title("Interest")
root.geometry("400x400")

frame=Frame(master=root, width=360, height=200, bg="#d0efff")

lbl1=Label(frame, text="Principal Amount", bg="#5895D3",fg='white', width=12)
lbl2=Label(frame, text="Time Period", bg="#5895D3",fg='white', width=12)
lbl3=Label(frame, text="Rate of Interest", bg="#5895D3",fg='white', width=12)

pr_entry=Entry(frame)
tp_entry=Entry(frame)
rt_entry=Entry(frame)

def display():
    pr= float(pr_entry.get())
    greet="You initially invested $"+ str(pr)
    tp = float(tp_entry.get())
    rt = float(rt_entry.get())
    simple_interest = str((pr*rt*tp)+pr)
    compound_interest= str((pr)*(1+rt)**tp)
    textbox.insert(END,greet + "\n")
    textbox.insert(END, "Value with simple interest = $"+simple_interest + "\n")
    textbox.insert(END, "Value with compounding interest = $"+compound_interest)

textbox=Text(bg="#BEBEBE",fg="black")

btn=Button(text="Calculate", command=display, fg='red')

frame.place(x=20,y=20)
lbl1.place(x=2,y=20)
pr_entry.place(x=150,y=20)
lbl2.place(x=20,y=80)
tp_entry.place(x=150,y=80)
lbl3.place(x=20,y=140)
rt_entry.place(x=150,y=140)
btn.place(x=180,y=210)
textbox.place(y=250)

root.mainloop()