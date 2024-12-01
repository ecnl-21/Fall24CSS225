import random
import globals
"""
Emely Chuy
This is the beginning of chapter 1
This will be the start of an introduction, making the user enter their name
"""
def chapter1():
    print("Arcade Days - Chapter 1: Valentine's Day")
#Player1 will be the users choice
    player1 = input("Please enter your chosen character name: ").strip()
    print(f"Hello, {player1}.")
#Player2 will always be Ben
    player2 = "Ben"

#This is to officially begin the story
    while True:
        start_game = input("Would you like to begin the game? (yes/no): ").strip().lower()
        if start_game == "yes":
            previous_choice = choose_action(player1, player2)
            break
        elif start_game == "no":
            print("Thanks for wanting to play!")
            return "q", 0
        else:
            print("Please enter 'yes' or 'no'.")


    print(f"{player1} will be {player2}'s friend.\nA strange string of events will commence now.")

    # List of days of the week
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    random_day = random.choice(days_of_week)

    print(f"Today is {random_day}. {player1} and {player2} wanted to go to the arcade today.")

    print(f"\nIt seems like {player2} took 'something' to ease the mind.")
    print(f"{player2} forgot about Valentine's Day. \nHis girlfriend was livid.\nYou are now entering an arcade.")

    return "C", previous_choice

#User will begin choosing options
def choose_action(player1, player2):
    game_over = False

    while not game_over:
        print("\nChoose an action:")
        print(f"1. {player1} will make conversation with {player2}.")
        print(f"2. {player1} will ignore {player2}.")
        print(f"3. Exit the game.")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(f"\nWhat will {player1} do?")
            print(f"1. Question {player2}.")
            print("2. Talk about what to play first.")
            print(f"3. Observe {player2}.")
            print("4. Change your mind and return to the main menu.")

            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                print(f"{player1}: Hey, {player2}, are you okay, dude? You seem kinda out of it.")
                response = random.choice([
                    "Yeah, I'm fine. Just going through it with my girlfriend right now.",
                    "No, something feels off. Don't know what it is.",
                    "Just tweaking really hard man, smoked too much."
                ])
                print(f"{player2} responds: '{response}'")

                if "girlfriend" in response:
                    print(f"{player1}: 'Dude, it's your fault your girlfriend's mad at you. You forgot about Valentine's Day.'")
                elif "something feels off" in response:
                    print(f"{player1}: '{player2}, maybe it's because your girlfriend's pissed at you. Literally the most important day for women.'")
                elif "smoked too much" in response:
                    print(f"{player1} decides to take {player2} to the hospital.")
                    game_over = True

            elif sub_choice == "2":
                print(f"{player1}: 'What should we play first, dude? There are so many games!'")
                print(f"{player2}: 'Maybe we can play Street Fighter? We haven't played that one in a while.'")
            elif sub_choice == "3":
                print(f"{player1} stays silent and observes {player2}.\n{player1} turns to John and they both shrug.")
            elif sub_choice == "4":
                print("Returning to the main menu.")
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            print(f"{player1} decides to question another group of friends about {player2}'s behavior.")
        elif choice == "3":
            print("Thanks for trying. Goodbye.")
            game_over = True
        else:
            print("Please enter a valid choice.")

    return choice
if __name__ == "__main__":
    player1, player2 = chapter1()
    if player1 and player2:
        choose_action(player1, player2)






