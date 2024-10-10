#Author: Emely Chuy
#10/9/2024

#The system will go from Fahrenheit to Celsius
def fahrenheit_to_celsius (fahrenheit):
    #The system will change from Fahrenheit to Celsius by using the calculation
    return (fahrenheit - 32) * 5/9

#The user will be asked to enter a number to use the calculation
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

#The system will convert to celsius
celsius = fahrenheit_to_celsius(fahrenheit)

#The system will print out what was calculated from Fahrenheit to Celsius
print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")

