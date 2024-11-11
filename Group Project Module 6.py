"""
Emely Chuy
11/11/2024

Group Project
"""

number = 3

guessed_number = int(input("Please guess a number between 1 and 10: "))

if guessed_number > 10:
    print("Invalid choice.")

elif guessed_number == number:
    print("Guessed number.")
elif guessed_number < number:
    print("Guess higher.")
elif guessed_number > number:
    print("Guess lower.")

else:
    print("Invalid choice.")


