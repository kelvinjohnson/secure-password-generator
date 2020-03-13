import string
import random


def generate_password():

    try:
        number_of_characters = int(input("Please enter the number of characters needed for password: "))
    except ZeroDivisionError:
        print('Sorry, you must have some characters for your password')
    except ValueError:
        print('Sorry, you entered an invalid value. Please enter a number')

    password = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits)])
    for number in range(number_of_characters):
        return password


print(generate_password())
