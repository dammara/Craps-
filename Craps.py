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
    print("How much money do you want to start with?")
    return int(input(">>> $"))


def bet():
    print("How much money do you want to wager?")
    return int(input(">>> $"))


def playGame():

    bank_roll = create()  # IMPORTANT!! Brings value typed and returned from create() and makes this line equal to create()

    if bank_roll <= 0:
        print("You cannot play without any cash. What a fucking broke boy!")
        print("No seriously, on everything, get your money up, not your funny up.")
        bank_roll = create()

    choice = 1  # This is the 'restart' checkpoint.

    while choice == 1:
        print(f"You have ${bank_roll}.")
        all_in = bet()

        while all_in > bank_roll or all_in <= 0:
            print("Invalid Bet, please place a real bet, you cheating bitch!!")
            all_in = bet()

        input(f"Okay, you wanna bet ${all_in}? Press ENTER to Roll a dice.")

        roll = roll_dice()

        print(f"You rolled a {roll}")

        if roll == 7 or roll == 11:
            bank_roll = bank_roll + all_in
            print(f"You got {roll} on the first try!")
            print(f"""You Win! Good Job bud.
            Now you have ${bank_roll}.
            Don't try walking out of here. I WILL rob you.""")
            if bank_roll <= 0:
                print("You ran out of money.")
            input()
            print('Wanna play again? Press 1 for Yes')
            choice = int(input(">>>"))
            if choice == 0:
                exit()
            if choice == 1 and bank_roll <= 0:
                print("Since you're of money, let's restart from the beginning")
                playGame()

        elif roll == 2 or roll == 3 or roll == 12:
            print("You lost. That's fucking embarrassing")
            bank_roll = bank_roll - all_in
            print(f"Now you have ${bank_roll}.")
            if bank_roll <= 0:
                print("You ran out of money.")
            print('Wanna play again, you gambling addict? Press 1 for Yes, 0 for NO')
            choice = int(input(">>>"))
            if choice == 0:
                exit()
            if choice == 1 and bank_roll <= 0:
                print("Since you're of money, let's restart from the beginning")
                playGame()
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
                print('Wanna play again? Press 1 for Yes, 0 for NO')
                choice = int(input(">>>"))
                if choice == 0:
                    exit()

            else:
                bank_roll = bank_roll - all_in
                print(f"You lost with a {roll}. Now you have ${bank_roll}.")
                input()
                if bank_roll <= 0:
                    print("You ran out of money.")
                print('Wanna play again, you gambling addict? Press 1 for Yes, 0 for NO')
                choice = int(input(">>>"))
                if choice == 0:
                    exit()
                if choice == 1 and bank_roll <= 0:
                    print("Since you're out of money, let's restart from the beginning")
                    playGame()


# Begin Game

# Splash Screen
print("HEY")
input()
print("Welcome to craps!")
input()
print("I heard your professor has a gambling problem.")
print("Let's try and make his addiction worse by gambling right in front of him.")
input()
print("Press 1 to play, Press 0 to protect your professor")
decide = int(input(">>>"))
if decide == 0:
    exit()
# execute, call defined functions
playGame()
