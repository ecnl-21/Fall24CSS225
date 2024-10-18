"""
Author: Emely Chuy
Date: 10/10/2024
"""

#The program will ask what the current wait time is
currentTimeStr = input("What is the current time (in hours 0-23)?")

#The program will ask the user how long they would like to wait
waitTimeStr = input("How many hours do you want to wait?: ")

#This will make an input string for current time to an integer
currentTimeInt = int(currentTimeStr)

#This will make the wait time into an integer
waitTimeInt = int(waitTimeStr)

#This will calculate the wait time and the current time, adding them
finalTimeInt = currentTimeInt + waitTimeInt

#This will print the results
print(finalTimeInt)
