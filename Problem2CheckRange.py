"""
Emely Chuy
11/10/2024

Problem 1

Write a Python function to check whether a number is in a given range. Use
range(1,10)
Print whether the number is in or not in the range

Tried out the try-except blocks for the first time. Somewhat similar
to if else statement.
"""



# Check if the number is within the range 1 to 9
def check_number_in_range(number):

   #If else statement will begin
   if number in range(1, 10):

      #Will print if number between 1-9 is in the range
      print(number, "is in the range.")
   else:

      #Will print if anything under or over the numbers 1-9
      print(number, "is not in the range.")


#Try-except blocks begin
try:
   #This will begin off the questions
   number = int(input("Choose a number: "))
   check_number_in_range(number)

   #This will pop up if user types in anything other than an integer
except ValueError:
   print("Please enter a valid integer.")






