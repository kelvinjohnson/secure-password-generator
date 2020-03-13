import string
from random import choice


def generate_password():

    while True:
        try:
            user_input = (int(input('Enter number of characters needed for password: ')))
            characters = string.ascii_letters + string.punctuation + string.digits
            password = "".join(choice(characters) for num in range(user_input))
            if user_input < 6:
                print('Your must enter a number no lower than 6')
            else:
                return password

        except ValueError:
            print('Invalid input. Please enter a number.')


print(f'''Password Generated Successfully: 
{generate_password()}''')

