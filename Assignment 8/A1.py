import tkinter as tk
from tkinter import ttk

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    subjects = []
    if math_var.get():
        subjects.append("Math")
    if sci_var.get():
        subjects.append("Sci")
    if eng_var.get():
        subjects.append("Eng")
    grade = grade_combobox.get()

    textbox.insert(tk.END, f"Name:{name}\n")
    textbox.insert(tk.END, f"Age:{age}\n")
    textbox.insert(tk.END, f"Gender:{gender}\n")
    textbox.insert(tk.END, f"Subjects:{','.join(subjects)}\n")
    textbox.insert(tk.END, f"Grade:{grade}\n")
    textbox.insert(tk.END, f"~"*40+"\n")

                       

root = tk.Tk()
root.title("Student form")
root.geometry("400x500")
tk.Label(root,text="Name:").place(x=20,y=20)
name_entry = tk.Entry(root, width =30)
name_entry.place(x=120,y=20)

tk.Label(root, text = "Age:").place(x=20,y=60)
age_entry = tk.Entry(root, width =30)
age_entry.place(x=120,y=60)

tk.Label(root, text = "Gender:").place(x=20, y =100)
gender_var = tk.StringVar(value = "None")
tk.Radiobutton(root, text = "Male", variable = gender_var, value ="Male").place(x=120,y=100)
tk.Radiobutton(root, text = "Female", variable = gender_var, value ="Female").place(x=180,y=100)

tk.Label(root,text="Subjects:").place(x=20,y=140)
math_var=tk.BooleanVar()
sci_var=tk.BooleanVar()
eng_var=tk.BooleanVar()
tk.Checkbutton(root,text="Math", variable = math_var).place(x=120,y=140)
tk.Checkbutton(root,text="Eng",variable = eng_var).place(x=120,y=170)
tk.Checkbutton(root,text="Sci",variable = sci_var).place(x=120,y=200)

tk.Label(root, text="Grade:").place(x=20,y=240)
grade_combobox = ttk.Combobox(root, values = ["A","B","C","D","E"],state = "readonly")
grade_combobox.place(x=150,y=240)

submit_button = tk.Button(root, text = "Submit", command = submit_form)
submit_button.place(x=150, y=280)

textbox = tk.Text(root, width = 40, height = 10)
textbox.place(x=20,y=320)

root.mainloop()