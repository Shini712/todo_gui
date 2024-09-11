import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

task_counter = 1 

def add_task():
    global task_counter
    task = task_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()
    if task != "":
        task_with_details = f"{task_counter}. {task} - Priority: {priority} - Due: {due_date}"
        task_listbox.insert(tk.END, task_with_details)
        task_entry.delete(0, tk.END)
        task_counter += 1 
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "No task selected")

def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, task + " (Completed)")
    except:
        messagebox.showwarning("Selection Error", "No task selected")

window = tk.Tk()
window.title("To-Do List")

task_entry = tk.Entry(window, width=40)
task_entry.pack(pady=10)

priority_label = tk.Label(window, text="Select Priority:")
priority_label.pack()
priority_var = tk.StringVar(value="Medium")
priority_dropdown = tk.OptionMenu(window, priority_var, "High", "Medium", "Low")
priority_dropdown.pack(pady=5)

due_date_label = tk.Label(window, text="Select Due Date:")
due_date_label.pack()
due_date_entry = DateEntry(window, selectmode='day', date_pattern='y-mm-dd', width=12)
due_date_entry.pack(pady=5)

add_button = tk.Button(window, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(window, text="Mark as Completed", width=20, command=mark_task_completed)
complete_button.pack(pady=5)

task_listbox = tk.Listbox(window, height=10, width=60)
task_listbox.pack(pady=10)

window.mainloop()