#Author: Emely Chuy
# 10/9/2024

#Ask the user for the amount of miles driver
miles_driven = float(input("Enter the number of miles driven: "))

#Ask the user the number of gallons of gas used
gas_used = float(input("Enter the number of gallons of gas used: "))

#The user will be calculating the miles per gallon
mpg = miles_driven / gas_used

#The system will print the result of the amount of car efficiency by driving
print(f"Your car's fuel efficiency is {mpg} MPG.")
