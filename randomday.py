"""
Emely Chuy
11/1/2024

Random Module, Problem # 3

 Use random.choice to select a day of the week from a list and print that day.
"""

#This will import the random module
import random

#List of days of the week
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Random.choice will help select a random day from the list up above
random_day = input(random.choice(days_of_week))

#This will the print a random day
print(random_day)