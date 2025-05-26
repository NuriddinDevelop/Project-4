from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class PromoCodeDiscount(DiscountStrategy):
    def apply_discount(self, price):
        promo_codes = {
            "PROMO10": 0.10,
            "PROMO20": 0.20,
            "PROMO30": 0.30
        }
        print(f"Promo kodlar: {tuple(promo_codes.keys())}")
        promo_code = input("Promo kodni kiriting: ")
        if promo_code not in promo_codes:
            print("Noto'g'ri promo kod. Iltimos, qaytadan urinib ko'ring.")
            return price
        
        for code, discount in promo_codes.items():
            if promo_code == code:
                print(f"Promo kodi {code} muvaffaqiyatli qo'llanildi!")
                return str(price * (1 - discount))

class LoyaltyDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return str(price * (1 - 0.15))

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return str(price)

def choice_discount(amount):
    discounts = [PromoCodeDiscount(), LoyaltyDiscount(), NoDiscount()]
    choice = input("Chegirma tanlang (1 - Promo kod, 2 - Sodiqlik, 3 - Hech qanday chegirma yo'q): ")

    if choice == "1":
        return discounts[0].apply_discount(amount)
    elif choice == "2":
        return discounts[1].apply_discount(amount)
    elif choice == "3":
        return discounts[2].apply_discount(amount)
    else:
        print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")
        return choice_discount()