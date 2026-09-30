import tkinter as tk
#create main window
window = tk.Tk()
window.title("Login System")
window.geometry("500x400")

#VAriables to store username and paswsword
username = ""
password = ""

#==============
#SAVE DATA
#==============
def save_data():
  global username, password

  #Get Values from Entry boxes
  username = username_entry.get()
  password = password_entry.get()

  #Move to Screen 2
  screen1.grid_forget()
  screen2.grid(row=0, column=0, padx=50, pady=50)

  #Display the saved values
  username_label.config(text="Username: "+ username)
  password_label.config(text="Password: " + password)


#============================
# SCREEN 1
#============================

screen1 = tk.Frame(window)
screen1.grid(row=0, column=0, padx=50, pady=50)

tk.Label(
  screen1,
  text="LOGIN SCREEN",
  font=("Arial", 20)
).grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(
  screen1,
  text="Username:"
).grid(row=1, column=0, padx=10, pady=10)


username_entry = tk.Entry(screen1, width=30)
username_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(
  screen1,
  text="Password:"
).grid(row=2, column=0, padx=10, pady=10)

password_entry = tk.Entry(
  screen1,
  width=30,
  show="*"
)


password_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(
  screen1,
  text="Save & Next",
  command = save_data
).grid(row=3, column=0, columnspan=2, pady=20)

#==============================
# SCREEN 2
#==============================

screen2 = tk.Frame(window)

tk.Label(
  screen2,
  text="WELCOME",
  font=("Arial", 20)
).grid(row=0, column=0, columnspan=2, pady=20)

username_label= tk.Label(
  screen2,
  text = "Username:"
)
username_label.grid(row=1, column=0, columnspan=2, pady=10)

password_label = tk.Label(
  screen2,
  text="Password:"
)
password_label.grid(row=1, column=0, columnspan=2, pady=10)


#start program
window.mainloop()