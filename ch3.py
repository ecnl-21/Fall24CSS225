import globals
import ch1
import ch2

"""
Beginning of chapter 5
"""
def chapter3(player1, player2):
    while True:
        start_ch3 = input("Would you like to begin chapter 3? (yes/no): ").strip().lower()
        if start_ch3 == "yes":
            previous_choice = choose_action(player1,player2)
            break
        elif start_ch3 == "no":
            print("Thanks for playing this far!")
            return 'q', 0
        else:
            print("Please enter 'yes' or 'no'.")
    return "C", previous_choice


#Choose action
def choose_action(player1, player2):


    print(f"\nAfter leaving the arcade, both left to the car without saying anything to anyone.")
    print(f"\n{player2} first said something, then {player1}")

    print(f"\n{player1}: Dude can I just ask? Like...what happened back there?")
    print(f"\n{player2}: Honestly... It's a lot.")

    choice = input(
        f"How will {player2} continue the conversation?\n"
        "1. 'I'm fine now, I think I took something that was a little too strong.'\n"
        "2. 'Maybe you should drive, I'm still feeling a little off after that.'\n"
        "3. 'I think we should grab a snack. I'm a little hungry now.'\n"
        "Enter your choice: "
    ).strip()

#Depending what someone chooses, it'll go to a certain sentence
    if choice == "1":
        print(f"\n{player1}: Okay, if you say so dude. I don't know where you went but jesus.")
    elif choice == "2":
        print(f"\n{player1} nods their head, switches seats so they can drive.")
    elif choice == "3":
        print(f"\n{player1} agrees, they go grab some pizza.")
    return choice


if __name__ == "__main__":
    chapter3("player1", "player2")
    choose_action("Emely", "Marianne")