# Sam and Ben
# Yahtzee
import random as rand

# Sets a variable which tells the user how many times they've tried to roll the dice for the section they've decided to persue. (Ex: They rolled it once, they rolled it twice, now three times)
attempts = 0

# Sets a variable which is used for the program to discern how many sections are available for the user to go through.(Ex: Chance, three of a kind, four of a kind,etc.) This just tells us how many sections there will be.
choices = 3
# Declares a list which will be used to determine if the user has already completed this section in the past. (Ex: If the user already has their ones filled out they should not be able to fill it out again.)
selected = [""]

# Creates a list that is as big as how many sections that are available for the user to go through Ex: Chance, three of a kind, four of a kind,etc.)
for i in range(choices):
    selected.append("")


def add_scores(ones, twos, threes, fours, fives, sixes, yahtzee, chance):
    total = ones + twos + threes + fours + fives + sixes + yahtzee + chance
    return (total)


def welcome():
    # start_game = int(input("Hello do you want to play yahtzee? (Press 1 to play or 2 to exit): "))
    start_game = 1
    if start_game == 1:
        print("Beginning a game of Yahtzee..")
        roll = [0, 0, 0, 0, 0]
        play_game(roll)
    else:
        print("Exiting the game..")
        exit()


# Runs through a for loop and appends a random integer to each element in the list so that we know which values the user rolled.
def roll_dice(roll):
    for i in range(len(roll)):
        roll[i] = rand.randint(1, 6)
    print("You rolled " + str(roll))


# Deals with each roll attempt to get better values in each section.
def rolls_for_turn(roll):
    global attempts
    # Asks the user if they are happy with their score. If not, they are free to roll again.
    final_score = int(input(
        "Would you like to use all of the numbers you rolled for your turn?\nPress 1 to end the turn:\nPress 2 to reroll the dice: "))
    if final_score == 1:
        pass
    # If the user chose to reroll make sure the user knows that they are using an additional attempt and reroll the dice. Rinse and repeat until attempt 3.
    elif final_score == 2:
        attempts +=1
        print("Attempt: " + str(attempts)); roll_dice(roll)
    return()


def play_game(roll):

    global attempts
    attempts += 1
    print("Attempt: " + str(attempts))

    roll_dice(roll)
    section_to_go_for = int(input("""Press 1 to go for your ones
Press 2 to go for your twos
Press 3 to go for your threes"""))

    # Verifies that the user hasn't already previously chosen the same selection to go for.
    if selected[section_to_go_for] == -1:
        print("You already have a score for this section! Please select another option.")
        play_game(roll)
    elif selected[section_to_go_for] != -1:
        choice = selected[section_to_go_for]
        selected[section_to_go_for] = -1
        while attempts < 3:
            rolls_for_turn(roll,choice)


welcome()


def user_spreadsheet():
    pass
