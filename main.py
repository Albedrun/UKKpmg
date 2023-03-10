from tkinter import *
import tkinter.font as font
root = Tk()
root.title("MyCalculator")

#definie font
myFont = font.Font(family='Courier', size=20, weight='bold')
myFontButton = font.Font(size=12, weight='bold')
#Create a textbox widget
layar = Entry(root, width=16, borderwidth=5, font=myFont)
layar.grid(column=0, row=0, columnspan=3)

def tambahAngka(angka):
    angkaPer = layar.get()
    layar.delete(0, END)
    layar.insert(0, str(angkaPer) + str(angka))

def clear():
    layar.delete(0, END)

def delete():
    length = len(layar.get())
    layar.delete(length-1, END)

def equal():
    angka_kedua = layar.get()
    layar.delete(0, END)

    if math == "plus":
        layar.insert(0, angkaFirst + float(angka_kedua))
    if math == "minus":
        layar.insert(0, angkaFirst - float(angka_kedua))
    if math == "divide":
        layar.insert(0, angkaFirst / float(angka_kedua))
    if math == "multiply":
        layar.insert(0, angkaFirst * float(angka_kedua))


def plus():
    angka_pertama = layar.get()
    layar.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = float(angka_pertama)
    math = "plus"

def minus():
    angka_pertama = layar.get()
    layar.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = float(angka_pertama)
    math = "minus"

def divide():
    angka_pertama = layar.get()
    layar.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = float(angka_pertama)
    math = "divide"

def multiply():
    angka_pertama = layar.get()
    layar.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = float(angka_pertama)
    math = "multiply"

angka0 = Button(root, text=0, padx=40, pady=20, command=lambda: tambahAngka(0), bg='orange', font=myFontButton, borderwidth=5)
angka1 = Button(root, text=1, padx=40, pady=20, command=lambda: tambahAngka(1), bg='orange', font=myFontButton, borderwidth=5)
angka2 = Button(root, text=2, padx=41, pady=20, command=lambda: tambahAngka(2), bg='orange', font=myFontButton, borderwidth=5)
angka3 = Button(root, text=3, padx=40, pady=20, command=lambda: tambahAngka(3), bg='orange', font=myFontButton, borderwidth=5)
angka4 = Button(root, text=4, padx=40, pady=20, command=lambda: tambahAngka(4), bg='orange', font=myFontButton, borderwidth=5)
angka5 = Button(root, text=5, padx=41, pady=20, command=lambda: tambahAngka(5), bg='orange', font=myFontButton, borderwidth=5)
angka6 = Button(root, text=6, padx=40, pady=20, command=lambda: tambahAngka(6), bg='orange', font=myFontButton, borderwidth=5)
angka7 = Button(root, text=7, padx=40, pady=20, command=lambda: tambahAngka(7), bg='orange', font=myFontButton, borderwidth=5)
angka8 = Button(root, text=8, padx=41, pady=20, command=lambda: tambahAngka(8), bg='orange', font=myFontButton, borderwidth=5)
angka9 = Button(root, text=9, padx=40, pady=20, command=lambda: tambahAngka(9), bg='orange', font=myFontButton, borderwidth=5)

dot = Button(root, text=".", padx=44, pady=20, command=lambda: tambahAngka("."), bg='orange', font=myFontButton, borderwidth=5)
clear = Button(root, text="Clear", padx=26, pady=20, command=clear, bg='#e0e0e0', font=myFontButton, borderwidth=5)
equal = Button(root, text="=", padx=40, pady=20, command=equal, bg='green', font=myFontButton , borderwidth=5)
plus = Button(root, text="+", padx=40, pady=20, command=plus, bg='yellow', font=myFontButton, borderwidth=5)
minus = Button(root, text="―", padx=37, pady=20, command=minus, bg='yellow', font=myFontButton, borderwidth=5)
delete= Button(root, text="<=", padx=36, pady=20, command=delete, bg='#e0e0e0', font=myFontButton, borderwidth=5)
divide = Button(root, text="/", padx=44, pady=20, command=divide, bg='yellow', font=myFontButton, borderwidth=5)
multiply = Button(root, text="x", padx=40, pady=20, command=multiply, bg='yellow', font=myFontButton, borderwidth=5)

angka1.grid(column=0, row=1)
angka2.grid(column=1, row=1)
angka3.grid(column=2, row=1)

angka4.grid(column=0, row=2)
angka5.grid(column=1, row=2)
angka6.grid(column=2, row=2)

angka7.grid(column=0, row=3)
angka8.grid(column=1, row=3)
angka9.grid(column=2, row=3)

angka0.grid(column=0, row=4)
dot.grid(column=1, row=4)
equal.grid(column=2, row= 4)

delete.grid(column=0, row=5)
clear.grid(column=1, row=5)
plus.grid(column=2, row=5)

minus.grid(column=0, row=6)
divide.grid(column=1, row=6)
multiply.grid(column=2, row=6)

root.mainloop()