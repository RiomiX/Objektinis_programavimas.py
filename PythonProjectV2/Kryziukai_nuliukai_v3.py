from tkinter import *

def pav():
    name = a
    return ['text'] == name


win = Tk()
win.title('<<<Kryziaus zygis>>>')
win.geometry('400x255')
win.resizable(False,False)

x_var = StringVar()
x_var.set(None)

# def fun():

for i in range(1, 10):
    if i % 2 == 0:
        a = 'O'
    else:
        a = 'X'

    b1 = Button(win, text='', width=10, height=5, activebackground='red', command=lambda : b1.config(text=a)).grid(row=1, column=1)
    b2 = Button(win, text='', width=10, height=5, activebackground='red', command=lambda b2: b2['text']).grid(row=1, column=2)
    b3 = Button(win, text='', width=10, height=5, activebackground='red', command=lambda b3: b3['text'] == a).grid(row=1, column=3)
    b4 = Button(win, text='', width=10, height=5, activebackground='red', command=lambda b4: b4['text'] == a).grid(row=2, column=1)
    b5 = Button(win, text='', width=10, height=5, activebackground='red', command=lambda b5: b5['text'] == a).grid(row=2, column=2)
    b6 = Button(win, text='', width=10, height=5, activebackground='red', command=lambda b6: b6['text'] == a).grid(row=2, column=3)
    b7 = Button(win, text='', width=10, height=5, activebackground='red', command=lambda b7: b7['text'] == a).grid(row=3, column=1)
    b8 = Button(win, text='', width=10, height=5, activebackground='red', command=lambda b8: b8['text'] == a).grid(row=3, column=2)
    b9 = Button(win, text='', width=10, height=5, activebackground='red', command=lambda b9: b9['text'] == a).grid(row=3, column=3)

# x_eile =Radiobutton(win, text='X eile rinktis', bg = 'lime', state=['disabled']).grid(row=1, column=5)
# o_eile =Radiobutton(win, text='O eile rinktis', bg = 'red', state=['disabled']).grid(row=2, column=5)

win.mainloop()