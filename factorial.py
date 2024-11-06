"""
Emely Chuy
11/1/2024

Random Module, Problem # 6

Use a for statement to calculate the factorial of a user input value.
Print this value as well as the calculated value
using the factorial function in the math module.
"""

import math

#User will type in a number
n = int(input("Enter a number: "))

#Calculate the factorial to use a for-loop
factorial = 1

for i in range (1, n + 1):
    factorial * i

#Print results
print("Factorial using for loop: ", factorial)
print("Factorial using math.factorial: ", math.factorial(n))