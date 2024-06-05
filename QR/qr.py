import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
import qrcode

def generate():
    txt = src_entry.get()
    qr = qrcode.QRCode(version=5, box_size=10, border=3)
    qr.add_data(txt)
    qr.make(fit=True)
    img = qr.make_image(fill_color='#4e4e4c', back_color='white').convert('RGB')
    img = img.resize((300, 300))  # Corrected the resize method
    img_tk = ImageTk.PhotoImage(img)
    qr_show_lbl.config(image=img_tk)
    qr_show_lbl.image = img_tk

win = tk.Tk()  # Changed ttkbootstrap.Window to tk.Tk
win.title("QR Code Generator")
win.geometry("400x450")  # Corrected the geometry method

app_icon = ImageTk.PhotoImage(file="QR/image.png")
win.iconphoto(False, app_icon)

src_lbl = ttk.Label(win, text="Enter text to convert URL")  # Corrected the variable name
src_lbl.pack(pady=10)
src_entry = ttk.Entry(win, width=50)  # Corrected the variable name
src_entry.pack()
btn = ttk.Button(win, text="Generate", command=generate)  # Corrected the button text and removed bootstyle
btn.pack(pady=10)
qr_show_lbl = ttk.Label(win)  # Corrected the variable name
qr_show_lbl.pack(pady=8)

win.mainloop()
