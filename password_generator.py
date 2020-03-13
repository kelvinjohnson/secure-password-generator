import string
from random import randint, choice


def generate_password():
    password = ''

    while True:

        try:
            user_input = (int(input('How many characters for you password?: ')))
            characters = string.ascii_letters + string.punctuation + string.digits
            password = "".join(choice(characters) for num in range(user_input))
            return password

        except ZeroDivisionError:
            print('Sorry, characters cannot be zero')
        except ValueError:
            print('You entered an invalid character. Please enter a number.')


print('New password:', generate_password())

