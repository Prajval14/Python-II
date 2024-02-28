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

player_data = [
    {'id': 1, 'name': 'dealer'},
    {'id': 2, 'name': 'player'}
]

cards_data = [
    {'name': 'ace', 'value': 1},
    {'name': 'two', 'value': 2},
    {'name': 'three', 'value': 3},
    {'name': 'four', 'value': 4},
    {'name': 'five', 'value': 5},
    {'name': 'six', 'value': 6},
    {'name': 'seven', 'value': 7},
    {'name': 'eight', 'value': 8},
    {'name': 'nine', 'value': 9},
    {'name': 'ten', 'value': 10},
    {'name': 'jack', 'value': 10},
    {'name': 'queen', 'value': 10},
    {'name': 'king', 'value': 10},
]

suits_data = [
    {'name': 'hearts', 'value': 'H'},
    {'name': 'spades', 'value': 'S'},
    {'name': 'diamond', 'value': 'D'},
    {'name': 'clubs', 'value': 'C'}
]

db.players.insert_many(player_data)
db.cards.insert_many(cards_data)
db.suits.insert_many(suits_data)

def createDeck():   
    deck = [] 
    cards_list = cards_collection.find()  
    suits_list = suits_collection.find()

    for card in cards_list:
        for suit in suits_list:
            deck.append({'name': card['name'], 'value': card['value'], 'suit': suit})
    
    random.shuffle(deck)

    return deck

def distributeCards(deck):  
    dealer_hand = []
    player_hand = []

    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())

    return dealer_hand

# Creating a flask application instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    initial_deck = createDeck()
    dealer_hand = distributeCards(initial_deck)
    return render_template('index.html', dealer_hand=dealer_hand)

if __name__ == '__main__':
    app.run(debug=True)