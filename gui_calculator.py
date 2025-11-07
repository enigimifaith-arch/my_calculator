
import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Result: {num1 + num2}")
    except ValueError:
        result_label.config(text="Error: Enter valid numbers")

def subtract_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Result: {num1 - num2}")
    except ValueError:
        result_label.config(text="Error: Enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")

# Input fields
tk.Label(root, text="First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons
tk.Button(root, text="Add", command=add_numbers).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract_numbers).pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the app
root.mainloop()