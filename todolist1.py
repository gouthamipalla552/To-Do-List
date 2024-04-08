import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Heading
        self.heading_label = tk.Label(master, text="To-Do List", font=("Helvetica", 12), fg="white", bg="blue")
        self.heading_label.pack(pady=10)

        # Task List
        self.task_list = tk.Listbox(master, width=50, height=10, font=("Helvetica", 12))
        self.task_list.pack(pady=5)

        # Entry
        self.entry = tk.Entry(master, width=50, font=("Helvetica", 12))
        self.entry.pack()

        # Buttons
        self.add_button = tk.Button(master, text="Add Task", bg="green", fg="white", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", bg="red", fg="white", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Populate list
        self.populate_list()

    def populate_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.populate_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete this task?")
            if confirmed:
                del self.tasks[selected_task_index[0]]
                self.populate_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoList(root)
    root.mainloop()
