import random

def get_int():
    num = input("Kiriting: ")
    if num.isdigit():
        return int(num)
    else:
        print("Iltimos son kiriting! ")
        return get_int()     

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789-_"
ids = []

def generate_id():
    id = ""
    for i in range(random.randint(5, 15)):
        id += random.choice(letters)
    if id in ids:
        return generate_id()
    ids.append(id)
    return id

def card_secret(card_num : str):
    card_num = list(card_num)
    card_num[6: -4] = '*' * 6
    num = card_num

    card_num = ""
    for i in num:
        card_num = card_num + i

    return card_num

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
