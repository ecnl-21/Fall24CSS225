# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

"""
Emely Chuy
10/15/2024
"""

#The user will be able to begin a string of numbers
year = int(input("Greetings! What is your year of origin?: "))

#The program will read this as if the year is less than or equal to 1900
if year <= 1900:
    #It will print this statement
    print("Woah, that's the past")

#The user can choose any year between 1900 to 2020
elif year >= 1900 and year <= 2020:
    #It will print this statement
    print ("That's totally the present!")

#This is the end of this if else string

else: #Anything that's not any of the numbers that was given above
      #Will print this statement
    print ("Far out, that's the future!!")
