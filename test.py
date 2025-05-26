# from transports import transpors

# tr = transpors.get_transport_and_price()
# print(f"Tanlangan transport: {tr[0]}, Narxi: {tr[1]} so'm")

from payments import payments

pay = payments.get_payment_processor()
pay.deposit()
# pay.deposit()
# pay.process_payment(20000)
# pay.process_payment(500000)