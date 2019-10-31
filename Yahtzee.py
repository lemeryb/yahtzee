# Sam and Ben
# Yahtzee
import random as rand


def add_scores(ones, twos, threes, fours, fives, sixes, threeofkind, fourofkind, smallstraight, yahtzee, chance):
    total = ones + twos + threes + fours + fives + sixes + threeofkind + fourofkind + smallstraight + yahtzee + chance
    return total


def welcome():
    input("Hello do you want to play yahtzee?"
          "press enter to play")
    print("Your goal is to beat the score of 230 and get as many points as you can")
    input("Press enter to roll the first 5 dice")



def user_spreadsheet():
