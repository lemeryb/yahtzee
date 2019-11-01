# Sam and Ben
# Yahtzee
import random as rand


def add_scores(ones, twos, threes, fours, fives, sixes, yahtzee, chance):
    total = ones + twos + threes + fours + fives + sixes + yahtzee + chance
    return total


def welcome():
    input("Hello do you want to play yahtzee?"
          "press enter to play")
    print("Your goal is to beat the score of 230 and get as many points as you can")
    input("Press enter to roll the first 5 dice")


def play_game():
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    yahtzee = 0
    chance = 0
    roll1 = rand.randint(1,6)
    roll2 = rand.randint(1,6)
    roll3 = rand.randint(1,6)
    roll4 = rand.randint(1,6)
    roll5 = rand.randint(1,6)
    roll6 = rand.randint(1,6)
    print(f"You rolled a {roll1}, a {roll2}, a {roll3}, a {roll4}, a {roll5}, and a {roll6}")
    if roll1 == roll2 == roll3 == roll4 == roll5 == roll6:
        print("Yahtzee that's 50 points!!")
        yahtzee = 50
    elif roll1 == roll2 == roll3 == roll4 == roll5 == 1 or roll2 == roll3 == roll4 == roll5 == roll6 == 1\
            or roll3 == roll4 == roll5 == roll6 == roll1 == 1 or roll4 == roll5 == roll6 == roll1 == roll2 == 1 \
            or roll5 == roll6 == roll1 == roll2 == roll3 == 1 or roll6 == roll1 == roll2 == roll3 == roll4 == 1:
        print("That was a pretty good roll you got 5 1's")
        answer = input("If you want to try and roll that last die again type Y or N")
        if answer == "Y" and yahtzee == 0:
            roll = rand.randint(1,6)
            if roll == 1:
                print("Yahtzee that's 50 points!!")
                yahtzee = 50






def user_spreadsheet():
