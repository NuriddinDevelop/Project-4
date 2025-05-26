from abc import ABC, abstractmethod
class Notifiable(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

class EmailNotification(Notifiable):
    def notify(self, message: str):
        print(f"Email orqali xabar yuborildi: {message}")

class SMSNotification(Notifiable):
    def notify(self, message: str):
        print(f"SMS orqali xabar yuborildi: {message}")

def get_notification_method(message):
    methods = ("Email", "SMS")
    method = input(f"Xabar yuborish usulini tanlang ({methods}):  ").strip().lower()

    if method == "email":
        return EmailNotification().notify(message)
    elif method == "sms":
        return SMSNotification().notify(message)
    else:
        print("Noto'g'ri xabar yuborish usuli tanlandi. Iltimos, 'email' yoki 'sms' ni tanlang.")
        return get_notification_method()