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
password = ""
password2 = ""
for letter in range (1, nr_letters + 1):
    password = (password + letters[random.randint(0, len(letters) - 1)])
    password2 += random.choice(letters)
for symbol in range (1, nr_symbols + 1):
    password = (password + symbols[random.randint(0, len(symbols) - 1)])
    password2 += random.choice(symbols)
for number in range (1, nr_numbers + 1):
    password = (password + numbers[random.randint(0, len(numbers) - 1)])
    password2 += random.choice(numbers)
print(password)
print(password2)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_order = ''.join(random.sample(password, len(password)))
print(random_order)
random_order2 = ''.join(random.sample(password2, len(password2)))
print(random_order2)

# this might be easier:
password_list = []
for letter in range (1, nr_letters + 1):
    password_list.append(random.choice(letters))
for symbol in range (1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for number in range (1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)