import tkinter as tk
#create main window
window = tk.Tk()
window.title("Login System")
window.geometry("500x400")

#VAriables to store username and paswsword
username = ""
password = ""

#==============
#SCREEN 1
#==============
def save_data():
  global username, password

  #Get Values from Entry boxes
  username = username_entry.get()
  password = password_entry.get()

  #Move to Screen 2
  screen1.place_forget()
  screen2.place(x=0, y=0, width=500, height=400)

  #Display the saved values
  username_label.config(text="Username: "+ username)
  password_label.config(text="Password: " + password)

screen1 = tk.Frame(window)
screen1.place(x=0, y=0, width=500, height=400)

title = tk.Label(
  screen1,
  text="LOGIN SCREEN",
  font=("Arial", 20)
)
title.place(x=120, y=30)

tk.Label(
  screen1,
  text="Username:"
).place(x=80, y=100)

username_entry = tk.Entry(screen1, width=30)
username_entry.place(x=180, y=100)

tk.Label(
  screen1,
  text="Password:"
).place(x=80, y=150)

password_entry = tk.Entry(
  screen1,
  width=30,
  show="*"
)

password_entry.place(x=180, y=150)

save_button = tk.Button(
  screen1,
  text="Save & Next",
  command = save_data
)
save_button.place(x=200, y=210)

#==============================
# SCREEN 2
#==============================

screen2 = tk.Frame(window)

tk.Label(
  screen2,
  text="WELCOME",
  font=("Arial", 20)
).place(x=190, y=40)

username_label= tk.Label(
  screen2,
  text = "Username:"
)
username_label.place(x=100, y=120)

password_label = tk.Label(
  screen2,
  text="Password:"
)
password_label.place(x=100, y=100)

#start program
window.mainloop()