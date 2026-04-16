##Importing the tkinter library to create a GUI application
import tkinter as tk

##Defining a function to handle button clicks
def click(num):
    result = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(result) + str(num))

##Creating the body of Calculator
root = tk.Tk()
root.title("Hello, User!")
root.geometry("600x400")
label = tk.Label(root, text="Welcome to Tkinter Calculator!")  
label.pack()
entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14))
entry.place(x=50, y=50)

##Creating buttons for numbers 0-9
btn_1 = tk.Button(root, text="1", width=5, height=2, command=lambda: click(1))
btn_1.place(x=10, y=220)

btn_2 = tk.Button(root, text="2", width=5, height=2, command=lambda: click(2))
btn_2.place(x=70, y=220)

btn_3 = tk.Button(root, text="3", width=5, height=2, command=lambda: click(3))
btn_3.place(x=130, y=220)

btn_4 = tk.Button(root, text="4", width=5, height=2, command=lambda: click(4))
btn_4.place(x=10, y=160)

btn_5 = tk.Button(root, text="5", width=5, height=2, command=lambda: click(5))
btn_5.place(x=70, y=160)

btn_6 = tk.Button(root, text="6", width=5, height=2, command=lambda: click(6))
btn_6.place(x=130, y=160)

btn_7 = tk.Button(root, text="7", width=5, height=2, command=lambda: click(7))
btn_7.place(x=10, y=100)  

btn_8 = tk.Button(root, text="8", width=5, height=2, command=lambda: click(8))
btn_8.place(x=70, y=100) 

btn_9 = tk.Button(root, text="9", width=5, height=2, command=lambda: click(9))
btn_9.place(x=130, y=100)

btn_0 = tk.Button(root, text="0", width=5, height=2, command=lambda: click(0))
btn_0.place(x=70, y=280)

#Defining functions for arithmetic operations and equal button
def equal():
    n2 = entry.get()
    entry.delete(0, tk.END)
    if math == "add":
        entry.insert(0, i + int(n2))
    elif math == "sub":
        entry.insert(0, i - int(n2))
    elif math == "mul":
        entry.insert(0, i * int(n2))
    elif math == "div":
        if int(n2) != 0:
            entry.insert(0, i / int(n2))
        else:
            entry.insert(0, "Error: Division by zero")

btn_equal = tk.Button(root, text="=", width=5, height=2, command=equal)
btn_equal.place(x=130, y=280)

def add():
    n1 = entry.get()
    global i
    global math
    math = "add"
    i = int(n1)
    entry.delete(0, tk.END)

btn_add = tk.Button(root, text="+", width=5, height=2, command=add)
btn_add.place(x=190, y=100)

def sub():
    n1 = entry.get()
    global i
    global math
    math = "sub"
    i = int(n1)
    entry.delete(0, tk.END)

btn_sub = tk.Button(root, text="-", width=5, height=2, command=sub)
btn_sub.place(x=190, y=160)

def mul():
    n1 = entry.get()
    global i
    global math
    math = "mul"
    i = int(n1)
    entry.delete(0, tk.END)

btn_mul = tk.Button(root, text="*", width=5, height=2, command=mul)
btn_mul.place(x=190, y=220)

def div():
    n1 = entry.get()
    global i
    global math
    math = "div"
    i = int(n1)
    entry.delete(0, tk.END)

btn_div = tk.Button(root, text="/", width=5, height=2, command=div)
btn_div.place(x=190, y=280)

def clear():
    entry.delete(0, tk.END)

btn_clear = tk.Button(root, text="AC", width=5, height=2, command=clear)
btn_clear.place(x=10, y=280)

#End Loop
root.mainloop() 
print("Tkinter window has been closed.")