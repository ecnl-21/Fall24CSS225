"""

Emely Chuy

This will import everything for it to work onto the other chapters. Globals was used for a bit
but was then dismissed and forgetting.
"""

import globals
import ch1
import ch2
import ch3
import ch4
import ch5
class Character:
    def __init__(self, player_name):  # Constructor
        self.player_name = player_name


    def __str__(self):
        return f"Player Name: {self.player_name}"

    def print_fav(self):
        print(f"The player is: {self.player_name}")

"""
Using the def main will begin the game
Starting off with "Hello, press Enter."
"""
def main():
    game_status = "C"
    globals.set_variables()
    player_name = input("Hello, press Enter.")
    player1 = Character(player_name)
    globals.print_ch1_message()
    game_status, previous_choice = ch1.chapter1()
    #Player 2 will always be Ben
    if game_status.lower() != 'q':
        globals.print_ch2_message()
        game_status, previous_choice = ch2.chapter2(player_name, "Ben")
        if game_status.lower() != 'q':
            globals.print_ch3_message()
            game_status, previous_choice = ch3.chapter3(player_name, "Ben")
            if game_status.lower() != 'q':
                game_status, previous_choice = ch4.chapter4(player_name, "Ben", previous_choice)
                if game_status.lower() != 'q':
                    game_status, previous_choice = ch5.chapter5(player_name, "Ben", previous_choice)
                    if game_status.lower() != 'q':
                        print("Congrats! You finished the game.")
                    else:
                        exit(5)
                else:
                    exit(4)
            else:
                exit(3)
        else:
            exit(2)
    else:
        exit(1)
        #When choosing to exit, exit(whatever number) will pop up

if __name__ == "__main__":
    main()
    #ch3.choose_action("Emely", "Marianne")