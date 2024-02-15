import random

class DeckOfCards:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = self.create_deck()

    def create_deck(self):
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                deck.append({'Suit': suit, 'Rank': rank})
        return deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def get_card_value(self, card):
        rank = card['Rank']
        if rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            return 10
        elif rank == 'Ace':
            # In Blackjack, Ace can be 1 or 11. For instance it as 11 here.
            return 11
    
    def get_card_from_shuffled_deck(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return "No cards left in the deck!" 

    def distribute_cards(self):
        dealerHand = [self.get_card_from_shuffled_deck(), self.get_card_from_shuffled_deck()]
        playerHand = [self.get_card_from_shuffled_deck(), self.get_card_from_shuffled_deck()]
        return dealerHand, playerHand
        
def main_menu():
    print("--> BlackJack <--\n")        
    userInput = input("1. Start Game\n2. Exit")
    try:
        userInput = int(userInput)
        return userInput
    except:
        return print(f"{userInput} is not a valid option")
    
def main():        
    deckObject = DeckOfCards()
    deckObject.create_deck()
    deckObject.shuffle_deck()   
    deckObject.distribute_cards() 

    for card in deckObject.distribute_cards.playerHand:
        print("Open Card:", card)

while True:
    userInput = main_menu()
    if userInput == 1:
        main()
    elif userInput == 2:
        print("Thank you. See you next time!")
        break
    else:
        print("Please select valid option")