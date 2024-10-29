from ast import Lambda
import math
import tkinter as tk  # Creating an abbreviation for tkinter

# Creating window
window = tk.Tk()
window.title("Simple Calculator")

# Creating input field
e = tk.Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # columnspan defines how many columns the button occupies

# Creating button addition function
def button_click(number):
    current = e.get()  # Every time I press a button, I capture the value already present
    e.delete(0, tk.END)  # Deleting the current value in the field
    e.insert(0, str(current) + str(number))  # Inserting the new value

# Function to clear screen
def button_clear():
    e.delete(0, tk.END)

# Function to add numbers
def button_add():
    first_number = e.get()
    global f_num  # Making it available outside of the function
    global math_operation  # Identifying which operation is in progress
    math_operation = "addition"
    f_num = float(first_number)
    e.delete(0, tk.END)

# Function for subtraction
def button_subtract():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    e.delete(0, tk.END)

# Function for multiplication
def button_multiply():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    e.delete(0, tk.END)

# Function for division
def button_divide():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    e.delete(0, tk.END)

# Function to calculate the result
def button_equal():
    second_number = e.get()
    e.delete(0, tk.END)
    
    if math_operation == "addition":
        e.insert(0, f_num + float(second_number))

    if math_operation == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math_operation == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math_operation == "division":
        if float(second_number) != 0:
            e.insert(0, f_num / float(second_number))
        else:
            e.insert(0, "Error: Div by 0")

# Defining buttons
button_1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = tk.Button(window, text="+", padx=39, pady=20, command=button_add)
button_equal = tk.Button(window, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = tk.Button(window, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(window, text="/", padx=41, pady=20, command=button_divide)

# Placing buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

window.mainloop()
