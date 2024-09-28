import tkinter as tk
from tkinter import messagebox
import json
import os

# File for saving the task list
TASK_FILE = "tasks.json"

# Save and load tasks to/from a JSON file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# GUI-based task manager
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        
        self.tasks = load_tasks()

        self.listbox = tk.Listbox(root, height=10, width=50)
        self.listbox.pack()

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()

        edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        edit_button.pack()

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack()

        complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_task_complete)
        complete_button.pack()

        self.display_tasks()

    def display_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Complete" if task["completed"] else "Incomplete"
            self.listbox.insert(tk.END, f"{task['name']} - {status}")

    def add_task(self):
        task_name = self.entry.get()
        if task_name:
            self.tasks.append({"name": task_name, "completed": False})
            self.entry.delete(0, tk.END)
            self.display_tasks()
            save_tasks(self.tasks)

    def edit_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            new_name = self.entry.get()
            if new_name:
                self.tasks[selected_index[0]]["name"] = new_name
                self.entry.delete(0, tk.END)
                self.display_tasks()
                save_tasks(self.tasks)

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.display_tasks()
            save_tasks(self.tasks)

    def mark_task_complete(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task["completed"] = not task["completed"]
            self.display_tasks()
            save_tasks(self.tasks)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
