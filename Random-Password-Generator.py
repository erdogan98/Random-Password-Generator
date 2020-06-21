import random

lower = 'abcdefghijklmnopqrstuvwxyx'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbol = '[]{}()*;/\,._-@&!§'

print("Welcome to the password generator."'\n'"Minimum 16 digits are recommended.\n")

all = lower + upper + number + symbol

length = input("How many characters do you want in your password?\n")
password = "".join(random.sample(all, int(length)))
               
print(password)
