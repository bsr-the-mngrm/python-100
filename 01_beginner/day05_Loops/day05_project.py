# DAY #05 - PyPassword Generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_pw = ""

for i in range(0, nr_letters):
    easy_pw += letters[random.randint(0, len(letters) - 1)]

for i in range(0, nr_symbols):
    easy_pw += symbols[random.randint(0, len(symbols) - 1)]

for i in range(0, nr_numbers):
    easy_pw += numbers[random.randint(0, len(numbers) - 1)]

print(f"Your easy password: {easy_pw}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_pw = ""
nr_char = nr_letters + nr_symbols + nr_numbers

for i in range(0, nr_char):
    character_set = random.randint(0,2)

    if character_set == 0:
        hard_pw += letters[random.randint(0, len(letters) - 1)]
    elif character_set == 1:
        hard_pw += symbols[random.randint(0, len(symbols) - 1)]
    else:
        hard_pw += numbers[random.randint(0, len(numbers) - 1)]

print(f"Your hard password: {hard_pw}")