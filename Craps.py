# Markhus Dammar
# 21 October 2019
# This program simulates a game of craps.

# init
from random import *

# definitions


def roll_dice():
    roll = (randint(1, 6) + randint(1, 6))
    return roll


def create():
    bank = print("How much money do you want to start with?")
    return int(input(">>> $"))


def bet():
    Ballin = print(f"How much money do you want to wager?")
    return int(input(">>> $"))

def playGame():
    bank_roll = create()  # IMPORTANT!! Brings value typed and returned from create() and makes this line equal to create()

    if bank_roll <= 0:
        print("You cannot play without any cash. What a fucking broke boy!")
        print("No seriously, on everything, get your money up, not your funny up.")
        bank_roll = create()
    choice = 1
    while choice == 1:

        all_in = bet()
        while all_in > bank_roll or all_in <= 0:
            print("Invalid Bet, please place a real bet, you cheating bitch!!")
            all_in = bet()

        input(f"Okay, you wanna bet ${all_in}? Press ENTER to Roll a dice.")

        while bank_roll > 0:
            roll = roll_dice()

            print(f"You rolled a {roll}")

            def the_replay():
                replay = input("Would you like to play again? (Y/N) >>>").title()

                if replay == "Y" or replay == "Yes":
                    print("Okay, let's play again.")
                    all_in = int(input(f"How much do you wanna bet out of your ${bank_roll}? >>> $"))

                elif replay == "N" or replay == "No":
                    print("Okay, have a nice day, LOSER")
                    input()
                    print("Oh, and thanks for the cash.")
                    input()
                    print(f"The computer takes your money. You now have $0!")
                    exit()

            if roll == 7 or roll == 11:
                bank_roll = bank_roll + all_in
                print(f"You got {roll} on the first try!")
                print(f"""You Win! Good Job bud.
                Now you have ${bank_roll}.
                Don't try walking out of here. I WILL rob you.""")
                input()
                print('Wanna play again? Press 1 for Yes, ENTER for No.')
                choice = int(input(">>>"))
                if choice == "":
                    exit()

            elif roll == 2 or roll == 3 or roll == 12:
                print("You lost. That's fucking embarrassing")
                input()
                print('Wanna play again, you gambling addict? Press 1 for Yes, ENTER for No')
                choice = int(input(">>>"))
                if choice == "":
                        exit()
            else:
                print(f"You got a {roll}, and must get {roll} again to win.")
                input()

                stored = roll
                roll = roll_dice()

                while roll != stored and roll != 7:
                    print(f"You got a {roll}, let's try again.")
                    input()
                    roll = roll_dice()

                if roll == stored:
                    bank_roll = bank_roll + all_in
                    print(f"You got a {roll} and won! You now have ${bank_roll}")
                    input()
                    print('Wanna play again? Press 1 for yes')
                    choice = int(input(">>>"))
                    if choice == "":
                        exit()
                else:
                    bank_roll = bank_roll - all_in
                    print(f"You lost with a {roll}. Now you have ${bank_roll}.")
                    input()
                    print('Wanna play again, you gambling addict? Press 1 for Yes, ENTER for No')
                    choice = int(input(">>>"))
                    if choice == "":
                        exit()

        print("Play again? Press 1 for Yes, ENTER for No.")
        choice = int(input())
        if choice == "":
            exit()











# Begin Game

# Splash Screen
# print("HEY")
#input()
# print("Welcome to craps!")
# input()
# print("I know you're bored as shit, so let's gamble all your cash away.")
# input()
# execute, call defined functions
# bank_roll = create()  # IMPORTANT!! Brings value typed and returned from create() and makes this line equal to create()

playGame()

# PROBLEMS --> Roll a good number; roll again crashes program.
