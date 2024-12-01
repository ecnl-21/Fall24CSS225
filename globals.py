
def print_ch1_message():
    print("Welcome to Arcade Days... You may want to increase your output screen...")


def print_ch2_message():
    print("Arcade Days - Chapter 2: Hallucinations")


def print_ch3_message():
    print("Arcade Days - Chapter 3: The Detour")

def print_ch4_message():
    print("Arcade Days - Chapter 4: The Truth")
def print_ch5_message():
    print("Arcade Days - Chapter 5: Home")

def set_variables():

    #print("Executing globals.....")

    global character
    global ch1_success
    global ch2_success
    global ch3_success
    global ch4_success
    global ch5_success

    ch1_success = True
    ch2_success = True

    character = "Emely"

if __name__ == "__main__":
    set_variables()