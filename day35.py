############### Our Blackjack House Rules #####################
#https://replit.com/@appbrewery/blackjack-final?embed=1&output=1#main.py

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
from replit import clear
from art import logo


#####FUNCTIONS#####
def deal_card():
  '''
  Generate random card from card deck
  '''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(list_of_cards):
  """
  calculate score from a list of cards
  """
  # Black Jack
  if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
    return 0  
  # greater than 21 but have an ace
  if 11 in list_of_cards and sum(list_of_cards) > 21:
    list_of_cards.remove(11)
    list_of_cards.append(1)
  return sum(list_of_cards)  

def compare(user_score, computer_score):
  """
  compare scores from user and computer to determine who win
  """
  if user_score > 21 and computer_score > 21:
    return "You went over, you lose."
  if (user_score == computer_score):
    return "It is a draw"
  elif computer_score == 0:
    return "You lose. Computer has a Blackjack."     
  elif user_score == 0:
    return "You win with a Blackjack!!! Yuhuhu"    
  elif user_score > 21:
    return "You went over, you lose."    
  elif computer_score > 21:
    return "Computer went over. You win!!!"     
  elif (user_score > computer_score):
    return "You win!!! Yuhuhu"
  elif (user_score < computer_score):
    return "Ohh you lose :("  


#####GAME FLOW#####
def playGame():
  """Game starts"""

  user_cards = []
  computer_cards = []
  isGameOver = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not isGameOver:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("Your cards: ", user_cards, ", current score: ",  user_score)
    print("Computer's first card: ", computer_cards[0])

    if user_score == 0 or computer_score == 0 or user_score > 21:
      isGameOver = True 
    else:
      user_continues = input("Type 'y' to get another card, type 'n' to pass: ")
      if (user_continues == 'y'):
        user_cards.append(deal_card())
      else:
        isGameOver = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


  print("Your final cards: ", str(user_cards), ", current score: ",  sum(user_cards))
  print("Computer's first card: ", str(computer_cards[0]))
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Black Jack?Type 'yay' or 'nay' to continue: ") == "yay":
  clear()
  print(logo)
  playGame()



