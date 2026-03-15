import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    roll = entry_roll.get()
    branch = entry_branch.get()
    email = entry_email.get()
    if not (name and roll and branch and email):
        messagebox.showwarning("Incomplete Data", "Please fill all fields.")
        return
    messagebox.showinfo("Submitted", f"Name: {name}\nRoll No: {roll}\nBranch: {branch}\nEmail: {email}")

root = tk.Tk()
root.title("Student Form")
root.geometry("300x300")

tk.Label(root, text="Student Form", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll No:").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Branch:").pack()
entry_branch = tk.Entry(root)
entry_branch.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Button(root, text="Submit", command=submit_form).pack(pady=15)

root.mainloop()