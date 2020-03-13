import string
import random

def generate_password(number_of_characters):

    number_of_characters = int(input("How many characters should your password be? "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits)])




