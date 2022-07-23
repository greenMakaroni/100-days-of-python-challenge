# Day 11 is a milestone project
# Your goal is to develop blackjack game in CLI

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_wins = 0
dealer_wins = 0
dealer_moves = ['draw', 'halt']
repeat = True


def drawCard(hand):
    hand.append(random.choice(cards))
    
def dealCards():
    drawCard(player_hand)
    drawCard(player_hand)

    drawCard(dealer_hand)
    drawCard(dealer_hand)



def showScoreAndHand():
    print("\nPlayer's hand: ", player_hand)
    print("Dealer's hand : ", dealer_hand)
    print("\nPlayer's score:",calculateScore(array=player_hand))
    print("Dealer's score:",calculateScore(array=dealer_hand))

def calculateScore(array):
    score = 0
    for card in array:
        if card == 11 and (score + 11) > 21:
            score += 1
        else:
            score += card
    return score

def make_move(move, hand, player):
    global didPlayerHalt
    global didDealerHalt

    if move == 'draw':
        drawCard(hand)
    elif move == 'halt':
        if player == 'player':
            didPlayerHalt = True
        elif player == 'dealer':
            didDealerHalt = True
        else:
            print("Incorrect player value")
    else:
        print("Incorrect move value")

def continueGame():       
    player_choice = input("Do you want to play another game? 'yes' / 'no': ")
    if player_choice == 'no':
        exit()
    elif player_choice != 'yes':
        continueGame()

while repeat:
    player_score = 0
    dealer_score = 0

    player_hand = []
    dealer_hand = []

    didPlayerHalt = False
    didDealerHalt = False

    player_bust = False
    dealer_bust = False

    dealCards()
    showScoreAndHand()

    while not didPlayerHalt or not didDealerHalt:
        if not didPlayerHalt:
            player_choice = input("Do you want to draw another card or halt? type: 'draw' or 'halt'")
            make_move(move=player_choice, hand=player_hand, player='player')
            if calculateScore(player_hand) > 21:
                dealer_wins += 1
                didPlayerHalt = True
                player_bust = True
                showScoreAndHand()
                print("\nPlayer bust!")
                print("***** Dealer wins! *****")
                continueGame()
                break
            
        if not didDealerHalt:
            dealer_choice = random.choice(dealer_moves)
            print("dealer choice ",dealer_choice)
            make_move(move=dealer_choice, hand=dealer_hand, player='dealer')
            if calculateScore(dealer_hand) > 21:
                player_wins += 1
                didDealerHalt = True
                dealer_bust = True
                showScoreAndHand()
                print("\nDealer bust!")
                print("***** You win! *****")
                continueGame()
                break

        if didPlayerHalt and didDealerHalt:
            if calculateScore(player_hand) == calculateScore(dealer_hand):
                showScoreAndHand()
                print("***** DRAW! *****")
                continueGame()
                break
            elif calculateScore(player_hand) > calculateScore(dealer_hand):
                player_wins += 1
                showScoreAndHand()
                print("***** You win! *****")
                continueGame()
                break
            else:
                dealer_wins += 1
                showScoreAndHand()
                print("***** Dealer wins! *****")
                continueGame()
                break
        else: 
            showScoreAndHand()

    





