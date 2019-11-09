# Simple Betting game
# Created by Ryan Hawkins
# 2019-11-09

import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_bet():
    try:
        bet = input("How much do you want to bet? ")
        if bet > bank:
            print()
            print(f"You don't have ${bet} to bet.")
            print("Try again.")
    except ValueError:
        print("Select a number amount.")
    return bet


bank = 1000
winnings = 0
losings = 0

played = False
keep_going = True

print("---" * 5)
print("Flip The Coin")
print("---" * 5)
print("written by")
print("Ryan Hawkins")
print()

while keep_going:

    print()
    print(f"Bank:  ${bank}")

    if played is False:
        play = input("Would you like to play? (Y/N) ").upper()
    else:
        play = input("Would you like to play again? (Y/N) ").upper()

    if play == "Y":

        clear()

        print(f"Bank:  ${bank}")

        bet = ""

        bet = int(input("Enter bet amount: "))

        if bet > bank:
            print()
            print(f"You don't have ${bet} to bet.")
            print("Try again.")
            continue

        choice = ""
        while choice != "0" and choice != "1":
            choice = input("Choose 0 or 1?: ")
        result = random.randint(0, 2)
        if choice == result:
            bank += bet
            winnings += bet
            losings -= bet
            print()
            print("You won.")
        elif choice != result:
            bank -= bet
            winnings -= bet
            losings += bet
            print()
            if bank <= 0:
                print("You lost all of your money.")
                print("You had to go to the ATM.")
                bank = 1000
            else:
                print("You lost.")

        played = True

    elif play == "N":
        clear()
        print("Thank you for playing.")
        if winnings > losings:
            print(f"You won a total of ${winnings}.")
        elif winnings < losings:
            print(f"You lost ${losings}.")
        else:
            print("You left without losing or gaining any money.")
        keep_going = False

    else:
        pass

print()
print("I hope you'll come back sometime soon.")
