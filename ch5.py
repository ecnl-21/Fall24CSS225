import ch1
import ch2
import ch3
import ch4

#This Chapter is more based on print statements, more about the story



def chapter5(player1, player2, previous_choice):
    while True:
     start_ch5 = input("Would you like to begin chapter 5? This is the end of the game. (yes/no): ").strip().lower()
     if start_ch5 == "yes":
        break
     elif start_ch5 == "no":
        print("Thanks for playing this far!.")
        return "q", 0
    else:
        print("Please enter 'yes' or 'no'.")

#Based on the previous choice from last chapter, all choices will still lead to Bens house

    if previous_choice == "1":
        print(f"\nThe car ride was quiet between {player1} and {player2} after their last exchanges.\nThey sit in the driveway of Ben's house.")
    elif previous_choice == "2":
        print(f"The roads are empty other than {player1} driving and {player2} sulking in his seat, lost in thought.")
    elif previous_choice == "3":
        print(f"After they grabbed pizza, they head to their car and go home to Ben's.")


    #Arriving to Ben's house
    #The story line

    print("The only light that illuminates is the porch and not a sound in the area happening.")
    print(f"\n{player1}: Alright, we're home now. Can we finally talked about what happened?")
    print(f"\n{player2} nods their head.'Okay... I owe you that much,'")
    print(f"\nBoth {player1} and {player2} step out of the car and go inside to sit on the couch.'")

    print(f"\n{player1}: 'Start from the beginning. What happened back at the arcade? Why were you freaking out so much? Was it what you smoked?'")
    print(f"\n{player2}: 'It wasn’t just the smoking... I've been having nightmares about it. But today, it was worse because of whatever I smoked.'")
    print(f"{player2} takes a deep breath. 'Those damn moles... they weren’t just moles to me. They were... talking.'")

    print(f"\n{player2} continues, 'They knew everything. About my girlfriend, about how I messed up Valentine’s Day... they were mocking me.'")
    print(f"{player2}: 'One of them said, \"'She’s better off without you'. Another said, 'You’re a failure.' And it felt... real.'")
    print(f"\n{player1} listens, concerned but composed. 'Ben, it sounds like you’ve been carrying a lot of guilt. \nMaybe it’s not the moles but everything you’ve been holding in.'")

    print(f"{player1}: 'Did you mess up? Yes, you did. But I think you gotta talk it out with her. I think you'll feel better.'")
    print(f"{player2}: 'But she's still mad at me. I don't think she'll listen to me.")
    print(f"{player1}: 'Well, sometimes you have to make people listen. She loves you, you love her. You'll figure it out.'")


    print(f"\n{player2} nods slowly. 'You’re probably right. \nI'll try talking with her and hopefully she'll listen. But it’s hard to shake how real it felt.'")
    print(f"\n{player1}: 'What matters now is that you’re safe and that we didn't actually take you to the hospital.'")
    print(f"{player2} sighs in relief. 'Yeah, you're right. Thanks, {player1}. I don’t know what I’d do without you.'")


    print(f"\n{player2}: 'Yeah I don't know either because you drive me insane.'")


    #The end of the game

    print("\n--- THE END ---")
    print("Thank you for playing!")


    return "C", 5



if __name__ == "__main__":
    chapter5()