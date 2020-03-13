import string
from random import choice, randint


def generate_password():

    while True:

        try:
            user_input = (int(input('Please enter the number of characters required: ')))
            characters = "".join(string.ascii_letters + string.punctuation + string.digits)
            password = ''.join(choice(characters)for num in range(randint(6, user_input)))
            return password

        except ZeroDivisionError:
            print('Sorry, characters cannot be zero')
        except ValueError:
            print('Sorry, you entered an invalid value. Please enter a number no lower than 6')


print('New password:', generate_password())

