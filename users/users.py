from abc import ABC, abstractmethod
from functions import *
from ticket import create_ticket_pdf, show_ticket
from payments.payments import *
from getpass import getpass
from notifications.notifications import *
from discounts.discounts import *
from functions import *
from transports.transpors import *

class User(ABC):
    def __init__(self):
        self.type = "User"

    @abstractmethod
    def get_user_info(self):
        pass

def create_add_login_and_password():
    login = input("Login kiriting: ")
    while True:
        password = getpass("Parol kiriting: ")
        password_again = getpass("Parol kiriting (takrorlang): ")
        if password != password_again:
            print("Parollar mos kelmadi. Iltimos, qaytadan urinib ko'ring.")
            continue
        if len(password) < 8:
            print("Parol kamida 8 ta belgidan iborat bo'lishi kerak. Iltimos, qaytadan urinib ko'ring.")
            continue
        break
    
    return login, password

customers = {}

class Customer(User):
    def __init__(self, name=None):
        super().__init__()
        if name is None:
            while True:
                name = input("Ismingizni kiriting: ")
                if len(name) < 3:
                    print("Ism kamida 3 ta belgidan iborat bo'lishi kerak. Iltimos, qaytadan urinib ko'ring.")
                    continue
                break
        self.name = name
        self.type = "Customer"
        self.customer_id = generate_id()
        self._card = get_payment_processor_method(self.customer_id)
        self.ticket = None
        customers[self.name] = self.customer_id, self._card, self


    def get_user_info(self):
        return f"Customer Name: {self.name}, Customer ID: {self.customer_id}"
admins = {}
class Admin(User):
    def __init__(self):
        super().__init__()
        self.__admin_id = generate_id()
        self.type = "Admin"
        self.login, self.password = create_add_login_and_password()
        admins[self.login] = self.password, self
    

    def cancel_ticket(self, ticket, customer):
        ticket = float(ticket)
        customer._card.cancel_payment(ticket[3])
        get_notification_method().send_notification(customer.name, "Chiptangiz muvaffaqiyatli bekor qilindi.")
        customer.ticket = None
        print("Chiptangiz muvaffaqiyatli bekor qilindi!")

    def get_user_info(self):
        return f"{self.type} Name: {self.login}"

yangi_vazifalar = {}

def admin_panel(admin: Admin):
    print("Admin paneliga xush kelibsiz!")
    
    for task, (ticket, customer) in yangi_vazifalar.items():
        if task == "Chipta olish":
            get_notification_method("Chipta muvaffaqiyatli sotib olindi.")
            customer.ticket = ticket
            print(f"{customer.name} uchun chipta muvaffaqiyatli sotib olindi.")
            yangi_vazifalar.pop(task)
        elif task == "Chiptani bekor qilish":
            admin.cancel_ticket(ticket, customer)
            print(f"{customer.name} uchun chiptani bekor qilish vazifasi bajarildi.")
            yangi_vazifalar.pop(task)

def admin_login():
    login = input("Admin login kiriting: ")
    password = getpass("Admin parol kiriting: ")
    if login not in admins:
        print("Bunday admin mavjud emas. Iltimos, qaytadan urinib ko'ring.")
        return admin_login(True)
    else:
        for admin_login, (admin_password, admin) in admins.items():
            if admin_login == login and admin_password == password:
                print(f"{admin.login} muvaffaqiyatli tizimga kirdi.")
                return admin_panel(admin)
            else:
                print("Noto'g'ri login yoki parol. Iltimos, qaytadan urinib ko'ring.")
                return admin_login()


def customer_panel(customer: Customer):
    print("Customer paneliga xush kelibsiz!")
    print("0. Chiqish")
    print("1. Chipta olish")
    print("2. Chiptani bekor qilish")
    print("3. Hisobni to'ldirish")
    
    choice = input("Tanlovingizni kiriting: ")
    
    if choice == "0":
        return
    elif choice == "1":
        transport, price = get_transport()
        date, time, route = get_date(), get_time(), get_route()
        discount = choice_discount(price)
        payment = make_payment(discount, customer.customer_id)
        if not payment:
            print("To'lov amalga oshirilmadi. Iltimos, qaytadan urinib ko'ring.")
            return customer_panel(customer)
        ticket = create_ticket_pdf(customer.name, customer.customer_id, transport, discount, route, date, time)
        
        show_ticket(ticket[0])
        yangi_vazifalar["Chipta olish"] =  ticket, customer
    elif choice == "2":
        yangi_vazifalar["Chiptani bekor qilish"] = customer.ticket, customer
    elif choice == "3":
        customer._card.deposit()
    else:
        print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")
        customer_panel(customer)

def customer_login():
    name = input("Ismingizni kiriting: ")
    if name not in customers:
        customer = Customer(name)
        customer_panel(customer)
    else:
        customer_id, card, customer = customers[name]
        print(f"{customer.name} muvaffaqiyatli tizimga kirdi.")
        return customer_panel(customer)

def main():
    print("0. Chiqish")
    print("1. Admin bo'lish")
    print("2. Customer bo'lish")
    print("3. Admin yaratish")
    choice = input("Tanlovingizni kiriting: ")
    if choice == "1":
        if len(admins) == 0:
            print("Admin mavjud emas. Iltimos, avval admin yarating.")
            return
        admin_login()
    elif choice == "2":
        customer_login()
    elif choice == "3":
        admin = Admin()
        print(f"Admin: {admin.login} muvaffaqiyatli yaratildi.")
    elif choice == "0":
        print("Dasturdan chiqish...")
        return False
    else:
        print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")
    