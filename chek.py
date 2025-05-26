import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import random
from PIL import Image, ImageTk
import tkinter as tk
import fitz
from functions import *

def show_chek(png_path):
    doc = fitz.open(png_path)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    root = tk.Tk()
    root.title("Chek")
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_img)
    label.pack()
    root.mainloop() 

def chek_pdf(amount_ballance: str, amount: int, card_num: str):
    png_path = f"Chek.png"
    size = (140 * mm, 155 * mm)
    c = canvas.Canvas(png_path, pagesize=size)
    width, height = size
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 10 * mm, " ----------------  Chek   ---------------- ")
    y = 130 * mm
    line_spacing = 12 * mm
    x_value = 20 * mm
    fields = [
        "Karta: UzCard",
        f"Karta raqami: {card_num}",
        f"Balans: {amount_ballance} so'm",
        f"To'lov sanasi: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"To'lov miqdori: {amount} so'm",
        f"Komissiya 0%",
        f"Jami: {amount}",
        f"Bankomat raqami: {random.randint(100000000, 999999999)}",
        "Bankomat nomi: TicketX Bankomat",
        "Tel: +998 (99)-999-99-99"
    ]
    c.setFont("Helvetica", 15)
    for value in fields:
        c.drawString(x_value, y, str(value))
        y -= line_spacing

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, 10 * mm, " ---------------- Raxmat ----------------" )
    
    c.save()

    show_chek(png_path)
    return png_path

def chek(amount_ballance: int = 0, card_num: str = "1234567890123456", bool: bool = False, amount: int = None):
        card_num = card_secret(card_num)

        if bool:
            chek_pdf(amount_ballance, amount, card_num)

        else:
            print("Chek chiqarilmadi.")

