from tkinter import *
import tkinter.messagebox
import math


root = Tk()
root.geometry("650x400+300+300")
root.title("Kalkulator UKK JAMAL")

switch = None

# Button on press


def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')

     
def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')


def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')


def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')


def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')

def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')


def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')


def btneq_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Value Error", "ini eror gan ")


# Label


disp = Entry(root, font="Verdana 20", fg="white", bg="#148F77", bd=1, justify=CENTER, insertbackground="#A2D9CE", cursor="arrow")
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 Buttons

btnrow1 = Frame(root)
btnrow1.pack(expand=TRUE, fill=BOTH)

btnc = Button(btnrow1, text="C", font="Segoe 23", relief=GROOVE, bd=5, command=btnc_clicked, fg="white", bg="#73C6B6")
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow1, text="⌫", font="Segoe 20", relief=GROOVE, bd=5, command=del_clicked, fg="white", bg="#73C6B6")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow1, text="=", font="Segoe 23", relief=GROOVE, bd=5, command=btneq_clicked, fg="white", bg="#73C6B6")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

btn1 = Button(btnrow2, text="1", font="Segoe 23", relief=RAISED, bd=0, command=btn1_clicked, fg="#0B5345", bg="#A3E4D7")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow2, text="2", font="Segoe 23", relief=RAISED, bd=0,  command=btn2_clicked, fg="#0B5345", bg="#A3E4D7")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow2, text="3", font="Segoe 23", relief=RAISED, bd=0, command=btn3_clicked, fg="#0B5345", bg="#A3E4D7")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow2, text="*", font="Segoe 23", relief=RAISED, bd=0, command=btnml_clicked, fg="#0B5345", bg="#A3E4D7")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow2, text="+", font="Segoe 23", relief=RAISED, bd=0, command=btnp_clicked, fg="#0B5345", bg="#A3E4D7")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)


btn4 = Button(btnrow3, text="4", font="Segoe 23", relief=GROOVE, bd=0, command=btn4_clicked, fg="#0B5345", bg="#A3E4D7")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow3, text="5", font="Segoe 23", relief=GROOVE, bd=0, command=btn5_clicked, fg="#0B5345", bg="#A3E4D7")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow3, text="6", font="Segoe 23", relief=GROOVE, bd=0, command=btn6_clicked, fg="#0B5345", bg="#A3E4D7")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow3, text="/", font="Segoe 23", relief=GROOVE, bd=0, command=btnd_clicked, fg="#0B5345", bg="#A3E4D7")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow3, text="-", font="Segoe 23", relief=GROOVE, bd=0, command=btnm_clicked, fg="#0B5345", bg="#A3E4D7")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

btn7 = Button(btnrow4, text="7", font="Segoe 23", relief=GROOVE, bd=0, command=btn7_clicked, fg="#0B5345", bg="#A3E4D7")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow4, text="8", font="Segoe 23", relief=GROOVE, bd=0, command=btn8_clicked, fg="#0B5345", bg="#A3E4D7")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow4, text="9", font="Segoe 23", relief=GROOVE, bd=0, command=btn9_clicked, fg="#0B5345", bg="#A3E4D7")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 23", relief=GROOVE, bd=0, command=btn0_clicked, fg="#0B5345", bg="#A3E4D7")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Segoe 21", relief=GROOVE, bd=0, command=dot_clicked, fg="#0B5345", bg="#A3E4D7")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)


root.mainloop()