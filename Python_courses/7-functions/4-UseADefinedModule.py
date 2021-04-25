# A Python module is just a code file containing files, constants, or services. You can split a
#  program into multiple code files to increase code modularity and reuse across the entire program.
#  Modules even let multiple programs share the same code.

# This exercise uses a module to separate code you might use in multiple apps.
#  The module separates code that implements your card deck from code that uses the card deck.



import DeckModule #represent the file in the same folder so functions car be easily splitted into the same folder

cards = DeckModule.create_deck()

for card in cards:
  print(card)