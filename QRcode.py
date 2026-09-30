#pip install qrcode pillow

import tkinter as tk
from tkinter import messagebox

try:
    import qrcode  # type: ignore[reportMissingModuleSource]
except ImportError as exc:
    raise SystemExit("qrcode is required. Install it with: pip install qrcode") from exc

try:
    from PIL import Image, ImageTk  # type: ignore[import-not-found]
except ImportError as exc:
    raise SystemExit("Pillow is required. Install it with: pip install pillow") from exc

# ---------- Logic (UNCHANGED) ----------
def generate_qr():
    data = entry.get().strip()
    if not data:
        messagebox.showwarning("Input needed", "Please enter some text")
        return

    qr = qrcode.QRCode(
        version=1,
        box_size=8,
        border=3
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#1f2933", back_color="white")

    tk_img = ImageTk.PhotoImage(img)
    qr_label.config(image=tk_img)
    qr_label.image = tk_img


# ---------- UI ----------
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("420x520")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

# Main card
card = tk.Frame(root, bg="white", bd=0, relief="flat")
card.place(relx=0.5, rely=0.5, anchor="center", width=360, height=460)

# Title
tk.Label(
    card,
    text="QR Code Generator",
    bg="white",
    fg="#111827",
    font=("Segoe UI", 18, "bold")
).pack(pady=(25, 5))

tk.Label(
    card,
    text="Enter text or link below",
    bg="white",
    fg="#6b7280",
    font=("Segoe UI", 10)
).pack(pady=(0, 15))

# Entry
entry = tk.Entry(
    card,
    font=("Segoe UI", 11),
    relief="solid",
    bd=1
)
entry.pack(ipady=6, padx=25, fill="x")

# Button
tk.Button(
    card,
    text="Generate QR Code",
    command=generate_qr,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    font=("Segoe UI", 11, "bold"),
    cursor="hand2"
).pack(pady=20, ipadx=10, ipady=6)

# QR display area
qr_frame = tk.Frame(card, bg="#f9fafb", bd=1, relief="solid")
qr_frame.pack(pady=10, padx=25, fill="both", expand=True)

qr_label = tk.Label(qr_frame, bg="#f9fafb")
qr_label.pack(expand=True)

root.mainloop()