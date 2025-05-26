from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from datetime import datetime
import random
from PIL import Image, ImageTk
import tkinter as tk
import fitz
from transports.transpors import *

ticket_nums = 0

def create_ticket_pdf(name: str, passport: str, transport_type: str = None, price: str = None, 
                      get_route=None, get_date=None, get_time=None):
    
    global ticket_nums
    ticket_num = str(ticket_nums + 1)
    ticket_nums += 1
    if len(ticket_num) == 1:
        ticket_num = "00" + ticket_num
    elif len(ticket_num) == 2:
        ticket_num = "0" + ticket_num

    price = str(price) + " so'm"

    route = get_route
    date = get_date
    time = get_time

    #TODO: png formatida saqlash

    png_path = f"TicketX_Chipta.png"
    c = canvas.Canvas(png_path, pagesize=landscape(A4))
    width, height = landscape(A4)
    c.setFillColor(colors.gold)
    c.rect(0, 0, width, height, fill=1)
    c.setFillColor(colors.white)
    background_image_path = "Chipta.jpg"
    c.drawImage(background_image_path, -70, -100, width=width + 140, height=height + 190)
    c.setFont("Helvetica-Bold", 40)
    c.drawCentredString(width / 2, height - 40 * mm, "TicketX - Chipta")
    c.setFillColor(colors.white)
    y = height - 70 * mm
    line_spacing = 13 * mm
    x_label = 30 * mm
    x_value = 270 * mm
    fields = [
        ("Foydalanuvchi", name),
        ("Passport raqami", passport),
        ("Transport", transport_type),
        ("Yo'nalish", route),
        ("Sana", date),
        ("Vaqt", time),
        ("Narx", price)
    ]
    for label, value in fields:
        c.setFont("Helvetica", 30)
        c.drawString(x_label, y, label + ":")
        c.setFont("Helvetica-Bold", 27)
        c.setFillColorRGB(0,0,255)
        c.drawRightString(x_value, y, str(value))
        c.setFillColor(colors.white)
        y -= line_spacing
    c.setStrokeColor(colors.white)
    c.line(25 * mm, 50 * mm, width - 25 * mm, 50 * mm)
    c.setFont("Helvetica-Bold", 100)
    c.setFillColorRGB(0,0,255)
    c.drawString(45 * mm, 22 * mm, ticket_num)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Oblique", 24)
    c.drawRightString(width - 105 * mm, 40 * mm, "Yaratilgan: ")
    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(0,0,255)
    c.drawRightString(width - 25 * mm, 40 * mm, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    c.save()

    return png_path, ticket_num, transport_type, price, route, date, time

def show_ticket(ticket_path):
    doc = fitz.open(ticket_path)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    root = tk.Tk()
    root.title("Bilet")
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_img)
    label.pack()
    root.mainloop()
