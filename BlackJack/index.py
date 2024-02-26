from flask import Flask, request, render_template
from pymongo import MongoClient
import random

# MongoDB configuration
client = MongoClient('localhost', 27017)
db = client['blackjack']
collection = db['players']
collection = db['cards']
collection = db['gamehistory']

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

db.players.insert_many(player_data)
db.cards.insert_many(cards_data)

# Creating a flask application instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)