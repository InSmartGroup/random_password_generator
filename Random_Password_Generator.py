import random
from sys import stderr


def choice(source, amount):
    for symbol in range(amount):
        password.append(random.choice(source))


numbers_list = [num for num in range(0, 10)]
letters_list = [letter for letter in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"]
symbols_list = [symbol for symbol in "~!`@#$%^&*()<>?"]

password = []

numbers_length = int(input("How many numbers do you want in your password: "))
choice(numbers_list, numbers_length)

letters_length = int(input("How many letters do you want in your password: "))
choice(letters_list, letters_length)

symbols_length = int(input("How many symbols do you want in your password: "))
choice(symbols_list, symbols_length)

random.shuffle(password)

generated_password = ""
for char in password:
    generated_password += str(char)

print("\nYour password:")
print(f"{generated_password}", file=stderr)
