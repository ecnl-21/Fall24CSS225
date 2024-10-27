#Emely Chuy
#10/26/2024

#This statement will still stay in the range of 1-50
for i in range(1,51):
    #Program will check to see if the number is divisible by 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    #Program will check to see if number is divisible by only 3
    elif i % 3 == 0:
        print("Divisible by three")
    # Program will check to see if number is divisible by only 5
    elif i % 5 == 0:
        print("Divisible by five")
    #Program will print i if there's a number that's not in the range
    else:
        print(i)