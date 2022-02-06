############### Blackjack Project #####################
import random
import art

print(art.logo)

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

computer_hand = []
user_hand = []
user_quits = False

def calculate_score(cards):
  """Calculates the score of both players"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

for _ in range(2):
  computer_hand.append(deal_card())
  user_hand.append(deal_card())

while not user_quits:
  user_score = calculate_score(user_hand)
  print(f"Your cards: {user_hand}")
  print(f"Your current score: {user_score}")
  computer_score = calculate_score(computer_hand)
  print(f"The computer's first card: {computer_hand[0]}")

  if user_score > 21 or user_score == 0 or computer_score == 0:
    user_quits = True
  else:
    user_draws_again = input("Type 'y' to draw another card, type 'n' to pass. ")
    if user_draws_again == "y":
      user_hand.append(deal_card())
    else:
      user_quits = True

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

