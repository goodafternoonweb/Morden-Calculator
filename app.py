import tkinter as tk
from tkinter import ttk
import math

# Function to evaluate the expression
def evaluate_expression():
    try:
        expression = entry_var.get()
        result = eval(expression, {"math": math, "sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log, "sqrt": math.sqrt, "pi": math.pi, "e": math.e})
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to update the entry field
def update_entry(value):
    entry_var.set(entry_var.get() + str(value))

# Function to clear the entry field
def clear_entry():
    entry_var.set("")

# Create the main window
root = tk.Tk()
root.title("Modern Scientific Calculator")
root.geometry("400x600")
root.configure(bg="#2b2b2b")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10, background="#3c3f41", foreground="white")
style.configure("TEntry", font=("Arial", 20))

# Entry field
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right', style="TEntry")
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
    ('sin', 'cos', 'tan', 'sqrt'),
    ('log', 'pi', 'e', '=')
]

button_frame = ttk.Frame(root, style="TFrame")
button_frame.pack(fill=tk.BOTH, expand=True)

for row in buttons:
    row_frame = ttk.Frame(button_frame)
    row_frame.pack(fill=tk.BOTH, expand=True)
    for button in row:
        if button == "=":
            cmd = evaluate_expression
        elif button == "C":
            cmd = clear_entry
        else:
            cmd = lambda val=button: update_entry(val)
        btn = ttk.Button(row_frame, text=button, command=cmd, width=6, style="TButton")
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

root.mainloop()
