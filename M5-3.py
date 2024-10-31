"""
Author: Emely Chuy
Date: 10/30/2024
"""

#This will start the turtle program

import turtle

#This will create a new window for the turtle to appear
wn = turtle.Screen()
#This will control the drawing operations
alex = turtle.Turtle()

#This will prompt in the output for the user to insert number of sides
sides = int(input("Number of sides?: "))
#Will allow user to put whole and decimals
length = float(input("Length of sides?: "))
#This will allow the user to put any color they want for the turtle to draw
colorname = input("Choice of color?: ")
#This will allow the user to put any color they want inside the polygon
fillcolor = input("Fill color?: ")

#This will set the color
alex.pencolor(colorname)
#This will set the filling color
alex.fillcolor(fillcolor)

#This will begin the filling of the shape
alex.begin_fill()


for i in range(sides):
    #This will make the turtle move forward
    alex.forward(length)
    #This will turn the turtle to the left
    alex.left(360/sides)

#This will end the filling of the shape
alex.end_fill()

#This will keep the turtle tab open till you choose to close it.
wn.mainloop()



