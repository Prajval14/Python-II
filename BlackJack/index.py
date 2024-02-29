from flask import Flask, request, render_template
from pymongo import MongoClient
import random

# MongoDB configuration
client = MongoClient('localhost', 27017)
db = client['blackjack']
players_collection = db['players']
cards_collection = db['cards']
suits_collection = db['suits']
history_collection = db['gamehistory']

# database_name = 'blackjack'
# client.drop_database(database_name)

# player_data = [
#     {'id': 1, 'name': 'dealer'},
#     {'id': 2, 'name': 'player'}
# ]

# cards_data = [
#     {'name': 'ace', 'value': 1},
#     {'name': 'two', 'value': 2},
#     {'name': 'three', 'value': 3},
#     {'name': 'four', 'value': 4},
#     {'name': 'five', 'value': 5},
#     {'name': 'six', 'value': 6},
#     {'name': 'seven', 'value': 7},
#     {'name': 'eight', 'value': 8},
#     {'name': 'nine', 'value': 9},
#     {'name': 'ten', 'value': 10},
#     {'name': 'jack', 'value': 10},
#     {'name': 'queen', 'value': 10},
#     {'name': 'king', 'value': 10},
# ]

# suits_data = [
#     {'name': 'hearts', 'value': 'H'},
#     {'name': 'spades', 'value': 'S'},
#     {'name': 'diamond', 'value': 'D'},
#     {'name': 'clubs', 'value': 'C'}
# ]

# db.players.insert_many(player_data)
# db.cards.insert_many(cards_data)
# db.suits.insert_many(suits_data)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_to_hand(self, card):
        self.hand.append(card)

    def calculate_score(self):
        self.score = 0
        for card in self.hand:
            self.score += card['value']
        return self.score

    def hit(self, deck):
        self.add_to_hand(deck.draw_card())
        return self.calculate_score()

    def stay(self):
        return self.calculate_score()
    
class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        for card in cards_collection.find():
            for suit in suits_collection.find():
                self.cards.append({'name': card['name'], 'value': card['value'], 'suit': suit['value']})

        random.shuffle(self.cards)     

        return self.cards   

    def draw_card(self):
        return self.cards.pop()
    
class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Player('Dealer')
        self.player = Player('Player')

    def start_game(self):
        self.deck.create_deck()

        self.dealer.hand.clear()
        self.player.hand.clear()
        self.dealer.add_to_hand(self.deck.draw_card())
        self.player.add_to_hand(self.deck.draw_card())
        self.player.add_to_hand(self.deck.draw_card())

        return self.deck.cards
    # def play_game(self):


    def determine_winner(self):
        dealer_score = self.dealer.calculate_score()
        player_score = self.player.calculate_score()

        if player_score > 21:  # Player busts
            return "Dealer"
        elif dealer_score > 21:  # Dealer busts
            return "Player"
        elif player_score == dealer_score:  # Tie
            return "Tie"
        elif player_score > dealer_score:  # Player wins
            return "Player"
        else:  # Dealer wins
            return "Dealer"
            
# Creating a flask application instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    game = BlackJackGame()    
    deck_instance = game.start_game()
    # print(len(game.deck.cards))
    dealer_hand = game.dealer.hand
    player_hand = game.player.hand
    # print(type(dealer_hand))
    return render_template('index.html', dealer_hand=dealer_hand, player_hand=player_hand, deck_instance=deck_instance)

@app.route('/hit', methods=['POST'])
def hit():
    player = Player(request.json.get('player_name'))
    deck = request.json.get('deck_instance')
    print(len(deck))
    score = player.hit(deck)
    print(score)

if __name__ == '__main__':
    app.run(debug=True)