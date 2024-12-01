"""
Emely Chuy
12/1/2024

Using a while loop, create a list called L that contains the numbers 0 to 10. On each
iteration, the loop should append the current value of a counter variable to the list and then
increase the counter by 1. The while loop should stop once the counter variable is greater than
10.

"""

#Empty list
L = []

counter = 0
#Start the while loop
while counter <= 10:
    L.append(counter)
    counter += 1
#Print the list
print(L)