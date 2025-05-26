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

def get_date():
    from datetime import datetime
    this_date = datetime.now()
    print("Hozirgi sana:", this_date.strftime("%Y-%m-%d"))
    date = input("Sana (MM-DD formatida): ")
    if date == "":
        print("Sana kiritilmadi. Iltimos, qaytadan urinib ko'ring.")
        return get_date()
    
    if not date[0:2].isdigit() or not date[3:5].isdigit() or date[2] != "-":
        print("Noto'g'ri sana formati. Iltimos, qaytadan urinib ko'ring.")
        return get_date()
    
    date = date.split("-")

    lst = []
    for index, i in enumerate(date):
        if i.isdigit():
            lst.append(int(i))
        else:
            print("Sana raqamlar bilan kiritilishi kerak. Iltimos, qaytadan urinib ko'ring.")
            return get_date()
    
    date = lst
    
    if date[0] < 1 or date[0] > 12 or date[1] < 1 or date[1] > 31:
        print("Noto'g'ri sana. Iltimos, qaytadan urinib ko'ring.")
        return get_date()
    
    if date[0] == 2 and date[1] > 29:
        print("Fevral oyida 29 kundan ko'p kun bo'lmaydi. Iltimos, qaytadan urinib ko'ring.")
        return get_date()
    
    if date[0] in [4, 6, 9, 11] and int(date[1]) > 30:
        print("Bu oyda 30 kundan ko'p kun bo'lmaydi. Iltimos, qaytadan urinib ko'ring.")
        return get_date()
    
    if date[0] == this_date.month and date[1] < this_date.day:
        print("Siz kiritgan sana hozirgi kundan oldin. Iltimos, qaytadan urinib ko'ring.")
        return get_date()
    
    if date[0] > this_date.month + 3 or (date[0] == this_date.month + 3 and date[1] > this_date.day):
        print("Transportga 3 oy ichida biletlar mavjud. Iltimos, qaytadan urinib ko'ring.")
        return get_date()

    if date[0] == 1:
        month = "Yanvar"
    elif date[0] == 2:
        month = "Fevral"
    elif date[0] == 3:
        month = "Mart"
    elif date[0] == 4:
        month = "Aprel"
    elif date[0] == 5:
        month = "May"
    elif date[0] == 6:
        month = "Iyun"
    elif date[0] == 7:
        month = "Iyul"
    elif date[0] == 8:
        month = "Avgust"
    elif date[0] == 9:
        month = "Sentabr"
    elif date[0] == 10:
        month = "Oktyabr"
    elif date[0] == 11:
        month = "Noyabr"
    else:
        month = "Dekabr"

    print("Siz kiritgan sana: ", month, " oyining ", date[1], " - kuni")
    string_date = str(str(month) + "-" + str(date[1]))
    return string_date

def get_route():
    routes = ["Samarqand", "Buxoro", "Andijon", "Toshkent", "Farg'ona", "Namangan", "Xorazm", "Qashqadaryo", "Surxondaryo", "Jizzax", "Sirdaryo", "Navoiy", "Qoraqalpog'iston"]
    locate = "Toshkent"
    print("Mavjud yo'nalishlar:", [route for route in routes if route != locate])
    routes = [route.lower() for route in routes]

    route = input("Yo'nalishni kiriting: ").lower()

    if route not in routes or route == locate:
        print("Noto'g'ri yo'nalish. Iltimos, qaytadan urinib ko'ring.")
        return get_route()
    
    route = str(locate + "dan =>" + route + "ga")

    return route

def get_time():
    times = ["02:00", "04:00", "06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]
    print("Mavjud vaqtlar:", times)

    time = input("Vaqt (HH:MM formatida): ")
    
    
    if not time[0:2].isdigit() or not time[3:5].isdigit() or time[2] != ":":
        print("Noto'g'ri vaqt formati. Iltimos, qaytadan urinib ko'ring.")
        return get_time()
    
    if time not in times:
        print("Noto'g'ri vaqt. Iltimos, qaytadan urinib ko'ring.")
        return get_time()
    
    return time

def create_ticket_pdf(name: str, passport: str, ticket_num: int):
    ticket_num = str(ticket_num)
    if len(ticket_num) == 1:
        ticket_num = "00" + ticket_num
    elif len(ticket_num) == 2:
        ticket_num = "0" + ticket_num
    
    transport_type, price = get_transport_and_price()

    price = str(price) + " so'm"

    route = get_route()
    date = get_date()
    time = get_time()

    #TODO: png formatida saqlash

    png_path = f"./tickets/TicketX_Chipta_{ticket_num}.png"
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

    return png_path

def show_ticket(png_path):
    doc = fitz.open(png_path)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    root = tk.Tk()
    root.title("Bilet")
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_img)
    label.pack()
    root.mainloop()
