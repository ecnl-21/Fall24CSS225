"""
Author: Emely Chuy
Date: 10/10/2024
"""""

#This will print this statement, so the user can type something in
greeting = input("Hello, possible pirate! What's the password?: ")

#If the user types in arrrr
if greeting in ("Arrr!"):
	#This will print
	print("Go away, pirate.")

	#If the user prints anything but arrr, they will receive this message
else:
	print("Greetings, hater of pirates!")
