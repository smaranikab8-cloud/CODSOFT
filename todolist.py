# -*- coding: utf-8 -*-
"""
Created on Sat May 23 02:05:53 2026

@author: hp
"""

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python To-Do List")
        self.root.geometry("400x450")

        # Define the UI Layout
        self.setup_ui()

    def setup_ui(self):
        # Header
        self.label = tk.Label(self.root, text="My Tasks", font=("Arial", 18, "bold"), pady=10)
        self.label.pack()

        # Entry box to add new tasks
        self.task_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.task_entry.pack(pady=10)
        self.task_entry.bind('<Return>', lambda event: self.add_task()) # Press Enter to add

        # Buttons Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.add_button = tk.Button(btn_frame, text="Add Task", command=self.add_task, bg="#4caf50", fg="white", width=10)
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", width=10)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(self.root, font=("Arial", 12), width=40, height=10, selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=20)

        # Update/Track Status Button
        self.complete_button = tk.Button(self.root, text="Mark as Done", command=self.mark_done, bg="#2196f3", fg="white", width=25)
        self.complete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, f"☐ {task}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_done(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            task_text = self.tasks_listbox.get(index)
            
            # Simple toggle/update logic
            if "☐" in task_text:
                new_text = task_text.replace("☐", "☑")
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, new_text)
                self.tasks_listbox.itemconfig(index, fg="grey")
            else:
                messagebox.showinfo("Info", "Task is already completed!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
