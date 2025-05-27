import tkinter as tk
from tkinter import messagebox, font

tasks = []  # List of (task, status) tuples

# Add task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append([task, "Incomplete"])
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Mark task as complete
def complete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index][1] = "Complete"
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark complete.")

# Update listbox with task and status
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task, status in tasks:
        display_text = f"{task}  [{status}]"
        task_listbox.insert(tk.END, display_text)

# GUI setup
root = tk.Tk()
root.title("To-Do List App with Status")
root.geometry("450x550")
root.configure(bg="#f0f8ff")  # Alice Blue

# Custom fonts
header_font = font.Font(family="Helvetica", size=18, weight="bold")
task_font = font.Font(family="Calibri", size=12)

# Title
title_label = tk.Label(root, text="📝 To-Do List", font=header_font, bg="#f0f8ff", fg="#333")
title_label.pack(pady=20)

# Entry
task_entry = tk.Entry(root, font=task_font, width=35, bg="#ffffff", fg="#000000", bd=2, relief="groove")
task_entry.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", font=task_font, bg="#4CAF50", fg="white", width=12, command=add_task)
add_button.grid(row=0, column=0, padx=5)

complete_button = tk.Button(button_frame, text="Mark Complete", font=task_font, bg="#2196F3", fg="white", width=15, command=complete_task)
complete_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", font=task_font, bg="#f44336", fg="white", width=12, command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

# Listbox
task_listbox = tk.Listbox(root, font=task_font, width=45, height=15, bd=2, relief="groove", selectbackground="#cce5ff")
task_listbox.pack(pady=15)

root.mainloop()
