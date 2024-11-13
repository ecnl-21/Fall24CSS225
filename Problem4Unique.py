"""
Emely Chuy

11/11/2024

Write a Python function that takes a list of numbers
and returns a new list with
unique elements of the first list.
Use list [1, 3, 3, 3, 6, 2, 3, 5].
Use the append function
"""

#Used a defined function for unique numbers
def unique_num(numbers):

    #Can store the unique numbers
    unique_list = []

#Will begin a loop for each numbers in the original list
    for number in numbers:

#This will make the program check to see if the number isn't on the list
        if number not in unique_list:

            #Will append the unique list
            unique_list.append(number)
    return unique_list

#Orginal list of numbers
numbers = [1, 3, 3, 3, 6, 2, 3, 5]

#This will add a new integer onto the list
numbers.append(25)

#Printing will begin
print(unique_num(numbers))

"""
All the numbers will print except duplicates, 
an added integer will be added to make a new list
"""
