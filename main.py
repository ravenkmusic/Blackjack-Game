############### Blackjack Project #####################
import random
import art
from replit import clear

print(art.logo)


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Calculates the score of both players"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose."
  if computer_score == user_score:
    return "You both have the same score. It's a draw."
  elif computer_score == 0:
    return "The computer got blackjack. You lose."
  elif user_score == 0:
    return "You got a perfect blackjack! You win!"
  elif user_score > 21:
    return "You busted. You lose."
  elif computer_score > 21:
    return "The computer's score went over. You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():
  computer_hand = []
  user_hand = []
  user_quits = False

  for _ in range(2):
    computer_hand.append(deal_card())
    user_hand.append(deal_card())

  calculate_score(user_hand)

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

  while computer_score != 0 and computer_score > 17:
    computer_hand.append(deal_card())
    computer_score = calculate_score(computer_hand)

  print(f"Your final hand: {user_hand} with a score of {user_score}. /n The computer's final hand: {computer_hand} with a score of {computer_score}.")
  print(compare(user_score, computer_score))

  #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you wanna play another round? Type 'y' or 'n'. "):
  clear()
  play_game()
