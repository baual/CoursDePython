# Use the technique from the previous unit to list every combination of suit and
#  rank in a set of 52 cards. Instead of just printing the value of the card, add
#  the card to a list that represents a deck of cards.

# When you finish, display the number of cards in the deck by using the function 
# that provides a count of items in the list.


suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck=[]

for  suit in suits:
  for rank in ranks:
    deck.append(f'{rank} of {suit}')
    #print(f'{rank} of {suit}')
    

print(len(deck))

print('step 2')


#Next, create a second list for the results of a deal. To simulate the dealing of five
#  random cards, use the appropriate method to choose a card. Add the card to the list
#  that represents the player's hand. Remove the card from the list that represents the deck.

#Before you simulate the deal, print this message:
# Dealing ...

#After you simulate the deal, print out the number of cards in the list that represents the
#  deck. Finally, print out the cards in the player's hand.

#When the process is complete, you should see something like the following output.
#  Your output will differ because the cards are dealt randomly.

# output expected:
# There are 52 cards in the deck.
# Dealing ...
# There are 47 cards in the deck.
# Player has the following cards in their hand:
# ['Jack of Hearts', 'Queen of Hearts', '4 of Spades', 'Ace of Hearts', '9 of Diamonds']
import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck=[]

for  suit in suits:
  for rank in ranks:
    deck.append(f'{rank} of {suit}')
    #print(f'{rank} of {suit}')
    
nbcard=len(deck)

print(f'There are {nbcard} cards in the deck.')

print('Dealing ...')

hand = []

while len(hand) < 5:
    card = random.choice(deck) #.choice permet de choisir un élément dans uen liste
    deck.remove(card)
    hand.append(card)

print(f'There are {len(deck)} cards in the deck.')
print('Player has the following cards in their hand:')
print(hand)