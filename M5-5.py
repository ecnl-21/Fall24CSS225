"""
Author: Emely Chuy
Date: 10/30/2024
"""
#Import turtle is to access the turtle program
import turtle

#This will begin the star program
star = turtle.Turtle()

#Turtle will turn right 75 degrees
star.right(75)
#Turtle will move forward 100 units
star.forward(100)

#The 'for' will begin a loop 4 times
for i in range(4):
    #Turtle will turn 144 degrees
    star.right(144)
    #Turtle will turn 100 units
    star.forward(100)

