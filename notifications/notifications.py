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