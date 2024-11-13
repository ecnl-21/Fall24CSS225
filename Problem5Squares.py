"""
Emely Chuy
11/11/2024

Problem 5
Using a chunk a code to make an image
"""
#Import the turtle program
import turtle

#Draw a square, t is turtle, side length is sz
def drawSquare (t, sz):

    for i in range (4):
        #Move the turtle forward
        t.forward(sz)
        #Move the turtle left by 90 degrees
        t.left(90)

#Set up the turtle window
wn = turtle.Screen()

#Turtle is named alex
alex = turtle.Turtle()

#Alex will be the color blue
alex.color("blue")
#The size of the square
size = 100

#This will program the system to make 4 squares
for _ in range (4):

    #Positioning the pen
    alex.penup()
    #Center the square on the screen
    alex.setposition(-size/2, -size/2)
    #Pen will start drawing
    alex.pendown()
    #Call the drawSquare for the current size
    drawSquare(alex, size)
    #Will reduce the square size by 20 for the next square
    size = size-20

wn.exitonclick()