#Author: Emely Chuy
#10/9/2024

#The term 'import' will help the user use the math module
import math

#The program will use the input statement to find the radius of the circle and so the user can print
radius = float(input("Please enter the radius of the circle:"))

#The program will use the math.pi variable to find the radius of a circl
area = math.pi * radius ** 2

#The program will print the statement to indicate the real answer of the radius of a circle
print(f"The area of the circle with a radius of {radius} units is {area:.2f} square units. Thank you for trying.")