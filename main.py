import random
import time
from turtle import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# bugs:
# when bust occurs, it's not ending the game and returning to input


print(logo)
def hit(list):
    """A function which takes in either the cards user/pc and adds a card from the deck """
    card_index = random.randint(0, len(cards) - 1)
    if card_index == 0:
        current_val = findValue(list)
        item = ""
        if current_val <= 10:
            list.append(1)
    item = int(cards[card_index])
    list.append(item)

def findValue(list):
    """A function which takes in either the cards of the user/pc and finds the value"""
    value = 0
    for i in list:
        value += int(i)
    return value

def checkScore(user_list, computer_list):
    """A function which takes in either the lists, calls the findValue function and compares the scores."""
    score_user = 0
    score_comp = 0
    score_user = findValue(user_list)
    score_comp = findValue(computer_list)
    if score_user > 21:
        print(f"You have {user_cards}")
        print("BUST! \nYou've lost")
        time.sleep(3)
        clear()
    elif score_comp > 21:
        print(f"Computer have {computer_cards}")
        print("You've won, Computer lost")
        time.sleep(3)
        clear()
    elif ((score_comp and score_user) > 21):
        print("You've lost")
        time.sleep(3)
        clear()

#need to put keepRunning at bottom of while after written to continue/stop loop
keepRunning = input("Do you want to play Blackjack? Type 'y' for yes or 'n' for no: ")
if keepRunning != ("y" or "n"):
    print("Unknown input, try running the game again")
    keepRunning = input("Do you want to play Blackjack? Type 'y' for yes or 'n' for no: ")
while(keepRunning == "y"):
    user_cards = []
    computer_cards = []
    hit(user_cards)
    hit(user_cards)
    hit(computer_cards)
    hit(computer_cards)
    choice = "h"
    while choice == "h":
        print(f"You have: {user_cards}")
        print(f"Computer currently has: {computer_cards[0]}")
        choice = input("Do you want to hit or stand? Type 'h' or 's': ")
        if choice == 'h':
            hit(user_cards)
            user_score = findValue(user_cards)
            checkScore(user_cards, computer_cards)
        elif choice == 's':
            print(f"Computer currently has: {computer_cards}")
            comp_score = findValue(computer_cards)
            while comp_score < 17:
                print("Computer chooses to hit")
                hit(computer_cards)
                print(f"Computer currently has: {computer_cards}")
                comp_score = findValue(computer_cards)
            user_score = findValue(user_cards)
            comp_score = findValue(comp_score)
            checkScore(user_cards, computer_cards)
        else:
            print("Unknown input was entered")
            choice = input("Do you want to hit or stand? Type 'h' or 's': ")
    keepRunning = input("Do you want to play Blackjack? Type 'y' for yes or 'n' for no: ")

