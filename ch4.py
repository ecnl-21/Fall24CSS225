import ch1
import ch2
import ch3
import globals

#This chapter will depend on the last chapters previous choice
def chapter4(player1, player2, previous_choice):
    while True:
     start_ch4 = input("Would you like to begin chapter 4? (yes/no): ").strip().lower()
     if start_ch4 == "yes":
        break
     elif start_ch4 == "no":
        print("Thanks for playing this far!.")
        return 'q', 0
    else:
        print("Please enter 'yes' or 'no'.")
#Depending on what the user chooses to do, it will go to the previous choice
    if previous_choice == "1": #Stayed in the car
        print(f"\n{player1} and {player2} choose to stay in the car. Only sound that is being made is the engine humming.")
        print(f"{player1}: 'Okay dude, are you finally going to tell me what the hell happened back there?'")
        print(f"{player2}: 'Okay but like... It's not going to sound right at all. I'm going to sound insane to you.'")
    elif previous_choice == "2": #Quiet car ride
        print(f"\n{player1} switches seats with {player2}, making {player1} the designated driver.")
        print(f"\n{player2} sinks into his seat, looking out the window blankly.")
        print(f"{player1}: 'So... we gonna talk about the crap you pulled back there or?'")
        print(f"{player2}: 'Hold on... Let me just figure it out myself because I really don't know what happened either.'")
        print(f"{player1}: 'Fine... But you have to tell me dude.'")
        print("They begin their car ride.")
    elif previous_choice == "3": #Pizzeria
        print(f"\nThe smell of greasy, warm pizza fills the air at the pizzeria, {player1} and {player2} sit at a small corner booth.")
        print(f"{player1}: 'Okay {player2}, you had your little snack, tell me what the hell happened back over there?'")
        print(f"{player2}: 'For your information, this little snack was delicious. But fine, I'll tell you since you keep bothering me about it.'")
        print(f"{player1}: 'Let's be so for real right now, who wouldn't?! You freaked out everyone back there including myself.'")


    #The storyline will be the same whether user chooses choice 1, 2, or 3
    #These clump of print statements is just the story
    print(f"\n{player2} hesitates, running his hair back.")
    print(f"{player2}: 'Promise me you won't judge me?'")
    print(f"{player1}: 'Dude, the amount of things we've gone through with each other, why would I?\nThe thing I'm really judging you on is the Valentine's Day thing to be honest.'")
    print(f"{player2}: 'Yeah yeah yeah. I know, I messed up. \nBut, okay I'll tell you.")

    print(f"\n{player2} sighs and looks at {player1}")
    print(f"{player2}: 'Okay we were obviously at the Wack-A-Mole game, I was having my fun till I started acting out.")
    print(f"{player2}: 'The moles... like they were just looking at me like... staring at me.")

    print(f"{player1} raises an eyebrow. 'It's taking a lot for me not to laugh at your face. They were staring at you? They're mechanical.'")
    print(f"{player2}: 'That's what I thought too till they began speaking to me and taunting me. They were telling me that I messed up things with my girlfriend.'")

    print(f"{player1}: 'Well I'm not surprised because you did mess up and we all know that you messed up big time your girlfriend this time.'")
    print(f"{player2}: 'Wait just hear me out'. {player2} lowers their voice to a whisper. \n'They were telling me things like, \"We know what you did. You won't be forgiven.\" ")


#The only choice option
    response = input(
        f"""
        How will {player1} respond?
        1. Laugh it off:
           'Dude, that's crazy!'
        2. Push it further:
           'Okay, tell me what else they said and saw.'
        3. Suggest a break:
           'Maybe you need a break from whatever the hell you just smoked.'

        Enter your choice: 
        """
    ).strip()
#If else statements

    if response == "1":
        print(f"\n{player1} laughs nervously. '{player2}, that's ridiculous, you may have not smoked the right thing.'")
        print(f"{player2}: 'Yeah... maybe. It just felt so weird, {player1}.")
    elif response == "2":
        print(f"\n{player1} leans towards {player2} and whispers 'Dude, I could have just told you yourself that you messed up big time. Let's get you to the hospital then see your girlfriend.'")
        print(f"{player2} shakes their head no. 'She's mad at me right now. \nIt's going to make it worse if I tell you I started hallucinating moles' from an arcade game speaking to me and taunting me.'")
    elif response == "3":
        print(f"\n{player1} places a hand on {player2}'s shoulder. 'Ben, maybe you’re just stressed. Let’s focus on relaxing for now.'")
        print(f"{player2} nods weakly. 'Yeah, you’re probably right. Thanks, {player1}.'")

    else:
        print("\nInvalid choice. The conversation trails off awkwardly as they sit in silence.")

    print("\nSomething about Ben’s story doesn’t sit right.")
    print("To be continued...")




    return "C", response

if __name__ == "__main__":
    chapter4("Emely", "Ben", 1)

