from users import users
import random

user = users.User
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789-_"

def get_int():
    num = input("Kiriting: ")
    if num.isdigit():
        return int(num)
    else:
        print("Iltimos son kiriting! ")
        return get_int() 

ids = []

def generate_id():

    id = ""
    for i in range(random.randint(5, 15)):
        id += random.choice(letters)
    if id in ids:
        return generate_id()
    ids.append(id)
    return id


