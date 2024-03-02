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

# Declaring and initializing variables (used in a game instance)
game_deck = [];
game_player_hand = [];
game_dealer_hand = [];
game_player_score = 0;
game_dealer_score = 0;

# Defining classes and related attributes and functions
class Players:
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
        new_card = deck.pop()
        self.add_to_hand(new_card)
        return new_card

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
        return self.cards.pop()
    
class Cards:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Players('dealer')
        self.player = Players('player')

    def start_game(self):
        self.deck.create_deck()
        
        self.deck.shuffle_deck()
        
        self.dealer.hand.clear()
        self.player.hand.clear()
        
        self.dealer.add_to_hand(self.deck.draw_card())
        self.player.add_to_hand(self.deck.draw_card())
        self.player.add_to_hand(self.deck.draw_card())

        self.dealer.calculate_score()
        self.player.calculate_score()

        return self.deck.cards
            
# Creating a flask application instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    global game_deck, game_dealer_hand, game_player_hand, game_dealer_score, game_player_score

    create_game = BlackJackGame()    
    game_deck = create_game.start_game()       
    game_dealer_hand = create_game.dealer.hand
    game_player_hand = create_game.player.hand
    game_dealer_score = create_game.dealer.score
    game_player_score = create_game.player.score

    return render_template('index.html',
    game_dealer_hand = game_dealer_hand, 
    game_player_hand = game_player_hand,
    game_dealer_score = game_dealer_score,
    game_player_score = game_player_score)

@app.route('/hit', methods=['POST'])
def hit():    
    global game_deck, game_dealer_hand, game_player_hand, game_dealer_score, game_player_score
    # print(len(game_deck))
    player = Players('player')
    player.hand = game_player_hand    
    # print('1', game_player_hand)
    # print('2', game_player_score)
    hit_card = player.hit(game_deck)
    # print(len(game_deck))
    game_player_hand = player.hand
    game_player_score = player.calculate_score()
    # print('3', game_player_hand)
    # print('4', game_player_score)
    print('5', hit_card)
    return jsonify(hit_card, game_player_score)

if __name__ == '__main__':
    app.run(debug=True)