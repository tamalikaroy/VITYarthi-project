# generator.py
import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password