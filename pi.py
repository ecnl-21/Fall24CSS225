"""
Emely Chuy
11/1/2024

Random Module, Problem # 4

Write a program to compute the approximation and then
print that value as well as the value of math.pi from the math module
"""

#Import the math module
import math

#Starting off with o
approx_pi = 0
#Ending with a good approximation number
num_terms = 1000

#Using the leibniz formula
for i in range(num_terms):
        #Using the leibniz formula
    approx_pi += ((-1 ** i)) / (2 * i + 1)

#Multiply by 4 for the final approximation of pi
approx_pi ** 4


#Printing the results
print("Approximation of pi:", approx_pi)
print("Value of math.pi: ", math.pi)


