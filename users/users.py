from abc import ABC, abstractmethod
from main import *
from ticket import create_ticket_pdf
class User(ABC):
    def __init__(self):
        name = input("Ismingizni kiriting: ")
        self.name = name
    @abstractmethod
    def get_user_info(self):
        pass


class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.customer_id = generate_id()

    def get_user_info(self):
        return f"Customer Name: {self.name}, Customer ID: {self.customer_id}"
    

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.admin_id = generate_id()

    def get_ticket(self):
        ticket = create_ticket_pdf()
        return ticket

    def get_user_info(self):
        return f"Admin Name: {self.name}, Admin ID: {self.admin_id}"