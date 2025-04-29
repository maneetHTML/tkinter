import tkinter as tk
from tkinter import messagebox

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Multiplication App")

# Create and place the widgets
label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the application
root.mainloop()
