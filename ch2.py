import globals



# class Character:
#     def __init__(self, player_name, fav_choice):  # Constructor
#         self.player_name = player_name
#         self.fav_choice = fav_choice
#
#     def __str__(self):
#         return f"Player Name: {self.player_name}, Favorite Choice: {self.fav_choice}"
#
#     def print_fav(self):
#         print(f"The player is: {self.player_name}, Favorite Choice: {self.fav_choice}")


def main():
    player1 = "Emely"
    player2 = "Ben"

    print(player1)
    print(player2)

    print(f"This is player 1: {player1}")
    print(f"This is player 2: {player2}")




def chapter2(player1, player2):
    """Hallucination begins at the 'Whack-a-Mole' game."""
    globals.ch2_success = None
    while True:
        start_ch2 = input("Would you like to begin Chapter 2? (yes/no): ").strip().lower()
        if start_ch2 == "yes":
            print("\nBeginning Chapter 2...")
            globals.ch2_success = True
            break
        elif start_ch2 == "no":
            print("Thanks for playing this far!")
            globals.ch2_success = False
            return "q", 0
        else:
            print("Please enter 'yes' or 'no'.")

    print(f"\n{player1} and {player2} walk over to the 'Whack-a-Mole' game.")
    print(f"\n{player2} tells {player1}, 'Let the master show you how it's done.'")

    print(f"\n{player2} inserts a coin, picks up the mallet, and starts hitting the moles.")
    print(f"After a few hits, {player2} begins behaving strangely, mumbling to himself.")
    print(f"{player1} notices {player2}'s face becoming pale, and his swings turning erratic.")

    hallucinations = [
        "The moles transform into tiny demons, start mocking Ben.",
        "The arcade lights start flashing and become distorted in a way.",
    ]

    print("\nSuddenly, Ben starts hallucinating:")
    for hallucination in hallucinations:
        print(f"- {hallucination}")

    print(f"\n{player1} tries to figure out what to do.")
    choice = input(f"How should {player2} respond?\n"
                   f"1. Grab the mallet from {player2} and yell, 'Dude, stop!'\n"
                   f"2. Call for help from the arcade staff.\n"
                   f"3. Try to distract {player2} by shouting his name loudly.\n"
                   "Enter your choice: ").strip()

    if choice == "1":
        print(f"\n{player2} grabs the mallet from {player1}.")
        print(f"{player1} stumbles back.")
        print(f"{player1}: 'What the... what just happened?'")

    elif choice == "2":
        print(f"\n{player2} rushes to get help from the arcade staff.")
        print("The staff quickly arrive and assist Ben, suggesting he take a break.")
        print(f"{player1} 'Dude, why would you call them? I'm fine.'")

    elif choice == "3":
        print(f"\n{player1} shouts, 'Ben!' as loudly as possible.")
        print(f"{player2} drops the mallet and looks around in confusion.")
        print(f"{player2}: 'Huh? What's going on'")

    else:
        print("\nInvalid choice. Ben's hallucination gets worse, and he collapses from exhaustion.")

    print("\nThe hallucination event leaves both players rattled. The next chapter will commence...")
    return "C", choice

if __name__ == "__main__":

    # Start the game
   # main()
   chapter2("Emely", "Ben")
