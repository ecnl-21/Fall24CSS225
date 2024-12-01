"""
Emely Chuy
12/1/2024

Using a while loop, ask the user to enter a number. Append each entered number
to a list and add them together. Continue asking for a number until the sum of the list of
numbers is greater than 100.
"""
#Empty list
numbers = []
total = 0 #Variable to keep track of sum

while total <= 100: #Continue until number is greater than 100
    number = int(input("Enter a number: ")) #Ask user for number
    numbers.append(number) #Append the number to the list
    total += number #Add number to the total

print(f"List of numbers: {numbers}")
print(f"Sum of numbers: {total}")

