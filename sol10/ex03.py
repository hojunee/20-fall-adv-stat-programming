from tkinter import *
from decimal import *
import math

cal = Tk()
cal.title = ("Calculator")

display = Entry(cal, width=40, bg="light green")
display.grid()

def factorial(n):
    return math.factorial(int(n))

def dec_to_bin(n):
    return format(int(n), "b")

def bin_to_dec(n):
    return int(n, 2)

def sqrt(n):
    return math.sqrt(float(n))

functions_dict = {
    '√' : sqrt,
    "!" : factorial,
    "DEC → BIN" : dec_to_bin,
    "BIN → DEC" : bin_to_dec
}

def click(key):
    if key == '=':
        try:
            result = str(eval(display.get()))[:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, " → ERROR!")
    elif key == "C":
        display.delete(0, END)
    elif key in functions_dict:
        try:
            result = display.get()
            display.delete(0, END)
            display.insert(END, str(functions_dict[key](result)))
        except:
            display.insert(END, " → ERROR!")
    else:
        display.insert(END, key)

top_row = Frame(cal)
top_row.grid(row=0, column=0, sticky=N)

display = Entry(top_row, width=40, bg="light green")
display.grid()

## Number Pad
num_pad = Frame(cal)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]

r = 0
c = 0

for btn_text in num_pad_list:
    def num_cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text, width=5, command=num_cmd).grid(row=r, column=c) 
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

## Function Pad
functions = Frame(cal)
functions.grid(row=1, column=0)

r = 0
c = 0
for btn_text in functions_dict:
    def fn_cmd(x=btn_text):
        click(x)
    Button(functions, text=btn_text, width=10, command=fn_cmd).grid(row=r, column=c) 
    r = r + 1

## Operator Pad
operator = Frame(cal)
operator.grid(row=1, column=0, sticky=E)
opr_pad_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C', 'π'
]

r = 0
c = 0

for btn_text in opr_pad_list:
    def opr_cmd(x=btn_text):
        if (x == 'π'):
            click("3.141592")
        else:
            click(x)
    Button(operator, text=btn_text, width=5, command=opr_cmd).grid(row=r, column=c) 
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

cal.mainloop()