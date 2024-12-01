"""
Emely Chuy
12/1/2024

Create a while loop that initializes a counter at 0 and will run until the counter
reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens.
Confirm the list results using a print statement.
"""

tens = [] #List to store variables by 10
counter = 0 #Start the counter

while counter <= 50: #Loop until the counter reaches 50
    if counter % 10 == 0: #If divisible by 10, add to list
        tens.append(counter)
    counter += 1 #Increment the counter

print(tens) #Display the result
