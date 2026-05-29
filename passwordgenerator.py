# -*- coding: utf-8 -*-
"""
Created on Sat May 23 02:12:06 2026

@author: hp
"""

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Password Generator")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Header
        tk.Label(self.root, text="Password Generator", font=("Arial", 16, "bold"), pady=20).pack()

        # Input Section
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter Password Length:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
        self.length_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
        self.length_entry.grid(row=0, column=1, padx=5)
        self.length_entry.insert(0, "12")  # Default length

        # Generate Button
        self.generate_btn = tk.Button(self.root, text="Generate Password", command=self.generate_password, 
                                      bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        self.generate_btn.pack(pady=20)

        # Result Display Section
        tk.Label(self.root, text="Generated Password:", font=("Arial", 10)).pack()
        self.password_display = tk.Entry(self.root, font=("Courier", 14), width=30, justify='center', 
                                         bd=0, bg="#f0f0f0", readonlybackground="#f0f0f0")
        self.password_display.pack(pady=10, ipady=5)

    def generate_password(self):
        try:
            # User Input: Prompt for length
            length = int(self.length_entry.get())

            if length < 4:
                messagebox.showwarning("Warning", "Length should be at least 4 for better security.")
                return

            # Generate Password: Use combination of random characters
            characters = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choice(characters) for _ in range(length))

            # Display the Password: Print to the screen
            self.password_display.config(state='normal')
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state='readonly')

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
