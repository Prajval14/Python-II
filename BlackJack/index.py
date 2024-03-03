from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import random

# -----------------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------------

# Defining classes and related attributes and functions
class Players:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_to_hand(self, card):
        self.hand.append(card)
        return card

    def calculate_score(self):
        self.score = 0        
        for card in self.hand:
            self.score += card['value']
        return self.score

    def stay(self):
        return self.calculate_score()
    
class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        for card in cards_collection.find():
            for suit in suits_collection.find():
                self.cards.append({'name': card['name'], 'value': card['value'], 'suit': suit['value']})                    
        return self.cards   

    def shuffle_deck(self):
        return random.shuffle(self.cards)             

    def draw_card(self):
        drawn_card = self.cards.pop()     
        return drawn_card

class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Players('dealer')
        self.player = Players('player')

    def declare_winner(self):
        if self.dealer.score > 21:
            return 'dealer-busted'
        elif self.player.score > 21:
            return 'player-busted'
        elif self.dealer.score == self.player.score:
            return 'tie'
        elif self.dealer.score > self.player.score:
            return 'dealer-win'
        elif self.player.score > self.dealer.score:
            return 'player-win'
        else:
            return 'game-error'
        

game_instance = BlackJackGame()

# Creating a flask application instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():       
    game_instance.deck.create_deck()

    game_instance.deck.shuffle_deck()

    game_instance.dealer.hand.clear()
    game_instance.player.hand.clear()

    game_instance.dealer.add_to_hand(game_instance.deck.draw_card())
    game_instance.player.add_to_hand(game_instance.deck.draw_card())
    game_instance.player.add_to_hand(game_instance.deck.draw_card())

    game_instance.dealer.calculate_score()
    game_instance.player.calculate_score()

    return render_template('index.html',
    game_dealer_hand = game_instance.dealer.hand, 
    game_player_hand = game_instance.player.hand,
    game_dealer_score = game_instance.dealer.score,
    game_player_score = game_instance.player.score)

@app.route('/hit', methods=['POST'])
def hit():    
    hit_card = game_instance.player.add_to_hand(game_instance.deck.draw_card())
    game_instance.player.calculate_score()
    return jsonify(hit_card, game_instance.player.score)

@app.route('/stay', methods=['POST'])
def stay(): 
    hit_cards = []
    while game_instance.dealer.score < 17:        
        hit_cards.append(game_instance.dealer.add_to_hand(game_instance.deck.draw_card()))
        game_instance.dealer.calculate_score()
    return jsonify(hit_cards, game_instance.dealer.score)

if __name__ == '__main__':
    app.run(debug=True)