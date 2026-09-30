import tkinter as tk
# create window
window = tk.Tk()
window.title("My screen")
window.geometry("500x400")

#Label
label = tk.Label(window, text="Enter your name")

#Entry
entry = tk.Entry(window)
entry.pack()

#Button
button = tk.Button(window, text= "Submit")
button.pack(pady=20)

# Keep window open
window.mainloop()