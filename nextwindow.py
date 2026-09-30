import tkinter as tk
# create window 
window = tk.Tk()
window.title("My application")
window.geometry("400x300")

screen1 = tk.Frame(window)
screen1.pack(fill="both", expand=True)
label1 = tk.Label(screen1, text="This is Screen 1")
label1.pack(pady=50)

def go_to_screen2():
    screen1.pack_forget()
    screen2.pack(fill="both", expand=True)
    
button1 = tk.Button(screen1, text="Go to Screen 2", command=go_to_screen2)
button1.pack(pady=20)

screen2 = tk.Frame(window)
label2 = tk.Label(screen2, text="This is Screen 2")
label2.pack(pady=50)

def go_to_screen1():
    screen2.pack_forget()
    screen1.pack(fill="both", expand=True)

button2 = tk.Button(screen2, text="Go to Screen 1", command=go_to_screen1)
button2.pack(pady=20)

# Start application
window.mainloop()