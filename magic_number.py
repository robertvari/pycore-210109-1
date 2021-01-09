import random

print("This is a simple number game")
print("What is my number? (0-10)")

secret_number = random.randint(0, 10)
# print(f"DEBUG: {secret_number}")
your_number = int(input("Your number?"))

while your_number != secret_number:
    print("You're wrong. Try again!")
    your_number = int(input("Your number?"))

print(f"You won! {secret_number} was my number.")