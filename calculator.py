# -*- coding: utf-8 -*-
"""
Created on Sat May 23 02:10:13 2026

@author: hp
"""

import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Calculator")
        self.root.geometry("400x350")
        self.root.config(padx=20, pady=20)

        # Header
        self.header = tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold"))
        self.header.pack(pady=10)

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # Number 1
        tk.Label(input_frame, text="Number 1:").grid(row=0, column=0, sticky="w")
        self.num1_entry = tk.Entry(input_frame, width=15)
        self.num1_entry.grid(row=1, column=0, padx=5, pady=5)

        # Number 2
        tk.Label(input_frame, text="Number 2:").grid(row=0, column=1, sticky="w")
        self.num2_entry = tk.Entry(input_frame, width=15)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        # Operation Choice
        tk.Label(root, text="Operation Choice:").pack()
        self.operation = ttk.Combobox(root, values=["Add", "Subtract", "Multiply", "Divide"], state="readonly")
        self.operation.set("Add")  # Default value
        self.operation.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)

        self.calc_btn = tk.Button(btn_frame, text="Calculate", command=self.calculate, bg="#4caf50", fg="white", width=10)
        self.calc_btn.grid(row=0, column=0, padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Clear", command=self.clear_fields, bg="#f44336", fg="white", width=10)
        self.clear_btn.grid(row=0, column=1, padx=5)

        # Result Display
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            # Get inputs
            n1 = float(self.num1_entry.get())
            n2 = float(self.num2_entry.get())
            op = self.operation.get()
            result = 0

            # Logic for operations
            if op == "Add":
                result = n1 + n2
            elif op == "Subtract":
                result = n1 - n2
            elif op == "Multiply":
                result = n1 * n2
            elif op == "Divide":
                if n2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = n1 / n2

            # Update Label
            self.result_label.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showwarning("Input Error", "Please enter valid numbers.")

    def clear_fields(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_label.config(text="Result: ")
        self.operation.set("Add")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
