# pip install mysql-connector-python

import tkinter as tk
from tkinter import messagebox
import mysql.connector

#connect to mysql
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

cursor = db.cursor()

#----------------------- SAVE DATA -----------------------
def save_data():
  username = username_entry.get()
  password = password_entry.get()
  if not username =="" or password =="":
    messagebox.showwarning("Warning ", "Enter username and password")
    return
  sql = "INSERT INTO users (username, password) VALUES (%s, %s)"

  cursor.execute(sql, (username, password))
  db.commit()

  messagebox.showinfo("Success", "Data saved successfully")
  username_entry.delete(0, tk.END)
  password_entry.delete(0, tk.END)

#-----------------------SHOW DATA -----------------------
def show_data():
  #Get data from MySQL
  cursor.execute("SELECT username, password FROM users")

  users = cursor.fetchall()

  #Create another window
  second_window = tk.Toplevel(window)
  second_window.title("Saved Users")
  second_window.geometry("400x300")

  tk.Label(
    second_window,
    text="Saved Users",
    font=("Arial", 18,)
  ).pack(pady=10)

  #display the data
  for user in users:
    username = user[0]
    password = user[1]

    tk.Label(
      second_window,
      text="Username: " + username + "password:  " + password,
      font=("Arial", 12)
    ).pack(pady=5)


#---------------------MAIN WINDOW-----------------------
window = tk.Tk()

window.title("User Registration")
window.geometry("400x300")

tk.Label(window, text="Username").pack(pady=5)

username_entry = tk.Entry(window)
username_entry.pack()

tk.Label(window, text="Password").pack(pady=5)

password_entry = tk.Entry(window, show="*")
password_entry.pack()

tk.Button(window, text="Save User", command=save_data).pack(pady=20)
tk.Button(window, text="Show Users", command=show_data).pack()

window.mainloop()