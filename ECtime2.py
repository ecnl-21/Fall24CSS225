"""
Author: Emely Chuy
Date: 10/18/2024
"""

#This will ask the user this statement, making it into a string
str_time = input("What time is it now?: ")

#This will ask the user this statement, making it into a string
str_wait_time = input("What is the number of hours to wait?:")

#This will make the string into an integer
time = int(str_time)

#This will make the string into an integer
wait_time = int(str_wait_time)

#This will add the integers and add them, making them the time
time_when_alarm_go_off = (time + wait_time)

#This will print the time
print(time_when_alarm_go_off)
