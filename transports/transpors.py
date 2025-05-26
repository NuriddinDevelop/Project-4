from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__(self):
        self.name = "Transport"

    def __str__(self):
        return f"{self.name} - {self.get_price[0]} so'm"

    @abstractmethod
    def get_transport_and_price(self):
        pass

class Train(Transport):
    def __init__(self):
        self.name = "Train"

    def get_transport_and_price(self):
        return 100000, self.name
    
class Flight(Transport):
    def __init__(self):
        self.name = "Flight"

    def get_transport_and_price(self):
        return 200000, self.name
    
class Bus(Transport):
    def __init__(self):
        self.name = "Bus"

    def get_transport_and_price(self):
        return 50000, self.name
    
def get_transport():
    transports = (Train(), Flight(), Bus())
    print(f"Mavjud transport turlari: {[transport.name for transport in transports]}")

    choice = input("Transport turini kiriting (Train, Flight, Bus): ").strip().lower()

    if not choice:
        print("Iltimos, transport turini kiriting.")
        return get_transport()
    
    if choice not in [transport.name.lower() for transport in transports]:
        print("Noto'g'ri transport turi. Iltimos, qaytadan urinib ko'ring.")
        return get_transport()
    
    for transport in transports:
        if choice == transport.name.lower():
            price, name = transport.get_transport_and_price()
            print(f"Siz tanlagan transport turi: {name}, narxi: {price} so'm")
            return name, price