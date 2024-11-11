"""
Emely Chuy
11/10/2024

Problem 1

Write a function areaOfCircle(r) which returns the area of a circle of radius r.

"""
#Math module will open
import math

#Function area of circle will calculate the area of a circle and the radius
def areaOfCircle(r):

    #Will calculate the area formula
    return math.pi * (r ** 2)

#Will ask user to enter radius of a circle, any number
radius = float(input("Enter the radius of the circle: "))

#Will print the formula, using the number user used
print("The area of the circle is:", areaOfCircle(radius))
