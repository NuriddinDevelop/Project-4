from abc import ABC, abstractmethod
import random
from chek import *
from main import *

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

    def withdraw(self, amount: int):
        if amount > self.__amount:
            print("Sizda yetarli mablag' yo'q.")
            return False
        self.__amount -= amount
        return True
    


class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        global card_secret
        withdraw = self.withdraw(amount)
        if withdraw:
            print(f"Kredit karta orqali {amount} so'm to'lov amalga oshirildi. Qolgan balans: {self.amount} so'm. Karta raqami: {card_secret(self.card_number)}")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        global card_secret
        withdraw = self.withdraw(amount)
        if withdraw:
            print(f"PayPal orqali {amount} so'm to'lov amalga oshirildi. Qolgan balans: {self.amount} so'm. Karta raqami: {card_secret(self.card_number)}")
        else:
            print("To'lov amalga oshirilmadi. Balansni tekshiring.")

class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount):
        global card_secret
        withdraw = self.withdraw(amount)
        if withdraw:
            print(f"Kripto to'lov orqali {amount} so'm to'lov amalga oshirildi. Qolgan balans: {self.amount} so'm. Karta raqami: {card_secret(self.card_number)}")
        else:
            print("To'lov amalga oshirilmadi. Balansni tekshiring.")

def get_payment_processor():
    processors = {
        "credit": CreditCardPayment,
        "paypal": PayPalPayment,
        "crypto": CryptoPayment
    }
    
    print("Mavjud to'lov tizimlari: ", list(processors.keys()))
    choice = input("To'lov tizimini tanlang (credit, paypal, crypto): ").strip().lower()
    
    if choice not in processors:
        print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")
        return get_payment_processor()
    
    return processors[choice]()
