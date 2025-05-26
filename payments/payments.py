from abc import ABC, abstractmethod
import random
from chek import *
from functions import *

card_numbers = []

def create_card_number():
    global card_numbers
    num = ""
    for _ in range(4):
        num += str(random.randint(1000, 9999))
    if num in card_numbers:
        return create_card_number()
    card_numbers.append(num)
    return num

cards = {}

class PaymentProcessor(ABC):
    def __init__(self):
        self.__card_number = create_card_number()
        self.__amount = 0

    @abstractmethod
    def process_payment(self, amount):
        pass

    @property
    def card_number(self):
        return self.__card_number

    @property
    def amount(self):
        return self.__amount


    def deposit(self):
        global chek
        print("To'lov summasini kiriting!")
        amount = get_int()
        if amount > 0:
            self.__amount += amount
            print(f"Hisobingiz {self.__amount} so'mga to'ldirildi.")
            bol = input("Chekni chiqarmoqchimisiz? (ha/yo'q): ").strip().lower()
            if bol == "ha":
                chek(self.amount, self.card_number, True, amount)
            elif bol == "yo'q":
                chek(False)
            else:
                print("Noto'g'ri javob. Chek chiqarilmaydi.")
        else:
            print("Yaroqsiz miqdor")

    def cancel_payment(self, amount: int):
        self.__amount += amount

    def withdraw(self, amount):
        if amount > float(self.__amount):
            print("Sizda yetarli mablag' yo'q.")
            choice = input(f"Tanlang (1: Hisobni to'ldirish, 2-to'lovni bekor qilish):")
            if choice == "1":
                self.deposit()
                return self.withdraw(amount)
            elif choice == "2":
                print("To'lov bekor qilindi.")
                return False
            else:
                print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")
                return self.withdraw(amount)
        self.__amount -= amount
        return amount
    
    def create_card(self, name: str):
        self.__card_number = create_card_number()
        cards[name] = self.__card_number, self
        print(f"Karta yaratildi. Karta raqami: {card_secret(self.__card_number)}")
        return self

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        global card_secret
        withdraw = self.withdraw(amount)
        if withdraw:
            print(f"Kredit karta orqali {amount} so'm to'lov amalga oshirildi. Qolgan balans: {self.amount} so'm. Karta raqami: {card_secret(self.card_number)}")
            return withdraw
        else:
            return False

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        global card_secret
        withdraw = self.withdraw(amount)
        if withdraw:
            print(f"PayPal orqali {amount} so'm to'lov amalga oshirildi. Qolgan balans: {self.amount} so'm. Karta raqami: {card_secret(self.card_number)}")
            return withdraw
        else:
            return False

class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount):
        global card_secret
        withdraw = self.withdraw(amount)
        if withdraw:
            print(f"Kripto to'lov orqali {amount} so'm to'lov amalga oshirildi. Qolgan balans: {self.amount} so'm. Karta raqami: {card_secret(self.card_number)}")
            return withdraw
        else:
            return False

def get_payment_processor_method(name):
    print("Qaysi to'lov usuli orqali karta ochmoqchisiz?")
    print("1. Kredit karta")
    print("2. PayPal")
    print("3. Kripto to'lov")

    choice = input("Tanlovingizni kiriting (1/2/3): ")
    if choice == "1":
        return CreditCardPayment().create_card(name)
    elif choice == "2":
        return PayPalPayment().create_card(name)
    elif choice == "3":
        return CryptoPayment().create_card(name)
    else:
        print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")
        return get_payment_processor_method(name)

def make_payment(price: int, name: str):
    if name not in cards:
        print("Sizda hali karta mavjud emas. Iltimos, avval karta yarating.")
        return None

    price = float(price)

    choice = cards[name][1].process_payment(price)
    if not choice:
        print("To'lov amalga oshirilmadi.")
        return None
    return choice
    
