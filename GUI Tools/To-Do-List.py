import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]["done"] = not tasks[selected]["done"]  # Toggle done status
        update_listbox()
    except IndexError:
        messagebox.showwarning("Select Error", "Please select a task to mark as done.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Select Error", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        display_text = f"✔ {task['task']}" if task["done"] else task["task"]
        listbox.insert(tk.END, display_text)

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30, font=('Arial', 14))
entry.pack(side=tk.LEFT, padx=(0, 10))

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=40, height=10, font=('Arial', 12))
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Mark Done", command=mark_done).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete Task", command=delete_task).pack(side=tk.LEFT, padx=5)

root.mainloop()



