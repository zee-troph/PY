import email
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# create window
window = tk.Tk()
window.title("Student registration form") 
window.geometry("500x600")

# Label + Entry for Name
label_name = tk.Label(window, text="Name:") 
name_entry = tk.Entry(window)
label_name.pack(pady=10)
name_entry.pack(pady=10)

tk.Label(window, text="Age:").pack(pady=10)
age_entry = tk.Entry(window)
age_entry.pack(pady=10)

email_entry = tk.Entry(window)
tk.Label(window, text="Email:").pack(pady=10)
email_entry.pack(pady=10)

#RADIOBUTTONS
tk.Label(window, text="Gender:").pack(pady=10)
gender_var = tk.StringVar()
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").pack(pady=5)
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").pack(pady=5)

#COMBOBOX
tk.Label(window, text="Select Department:").pack(pady=10)
course_var = tk.StringVar()
course_combo = ttk.Combobox(window, textvariable=course_var)
course_combo['values'] = ("Computer Science", "Mathematics", "Physics", "Chemistry")
course_combo.pack(pady=10)
# CHECKBOX
tk.Label(window, text="Select your interests:").pack(pady=10)
interest_var1 = tk.IntVar()
tk.Checkbutton(window, text="Programming", variable=interest_var1).pack(pady=5)
python = tk.BooleanVar()
javascript = tk.BooleanVar()
html = tk.BooleanVar()
tk.Checkbutton(window, text="Python", variable=python).pack(pady=5)
tk.Checkbutton(window, text="JavaScript", variable=javascript).pack(pady=5)
tk.Checkbutton(window, text="HTML/CSS", variable=html).pack(pady=5)
# TEXTAREA
tk.Label(window, text="Additional Comments:").pack(pady=10)
address_text = tk.Text(window, height=5, width=40)
address_text.pack(pady=10)
#button
def submit_form():
    skills= []
    if python.get():
        skills.append("Python")
    if javascript.get():
        skills.append("Javascript")
    if html.get():
        skills.append("HTML/CSS")
        
    messagebox.showinfo(
        "Student information", f"Name: {name_entry.get()}\n"
        f"Email: {email_entry.get()}\n"
        f"Age: {age_entry.get()}\n"
        f"Gender: {gender_var.get()}\n"
        f"Department: {course_var.get()}\n"
        f"Interests: {', '.join(skills) if skills else 'None'}\n"
        f"Comments: {address_text.get('1.0', tk.END).strip()}"
    ) 
    
submit_button = tk.Button(
    window,
    text="submit",
    width=20,
    command=submit_form
)                
submit_button.pack(pady=20)

#Start application
window.mainloop()
        
