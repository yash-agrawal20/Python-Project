#Password Generator Project
#Date:- 10/08/2021
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

total_elements = nr_letters + nr_symbols + nr_numbers
easy_pass = ""
list = []
for number in range(0,nr_letters):
  list.append(random.choice(letters))
for number in range(0,nr_symbols):
  list.append(random.choice(symbols))
for number in range(0,nr_numbers):
  list.append(random.choice(numbers))
for number in range(0,total_elements):
  easy_pass = easy_pass + list[number]

print(f"Easy Password: {easy_pass}\n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_pass = ""
#random.shuffle(list)
# or
list_hard = random.sample(list,len(list))
# for number in range(0,total_elements):
#   list_hard.append(random.choice(list))
for number in range(0,total_elements):
  #hard_pass = hard_pass + list[number]
  #or
  hard_pass = hard_pass + list_hard[number]
print(f"Hard Password: {hard_pass}\n")
