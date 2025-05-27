# from transports import transpors

# tr = transpors.get_transport_and_price()
# print(f"Tanlangan transport: {tr[0]}, Narxi: {tr[1]} so'm")

# from payments import payments

# pay = payments.get_payment_processor()
# pay.deposit()
# pay.deposit()
# pay.process_payment(20000)
# pay.process_payment(500000)

# from users import users
# admin = users.Admin()
# print(admin.get_user_info())

dict1 = {
    "Apple": (10, "Fruit"),
    "Carrot": (5, "Vegetable"),
    "Banana": (8, "Fruit"),
    "Broccoli": (7, "Vegetable"),
    "Orange": (12, "Fruit"),
}

for key, (amaunt, type) in dict1.items():
    print(f"{key} - {amaunt} so'm, {type}")
    