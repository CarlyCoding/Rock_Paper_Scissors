from flask import render_template
from app import app
from models.game import Game
from models.player import Player



@app.route('/home')
def index():
    return render_template('index.html')

@app.route('<player1_choice>/<player2_choice>')
def rock_paper_scissors(player1_choice, player2_choice):
    player1 = Player("Stanley Kubrick", player1_choice)
    player2 = Player("Taika Waititi", player2_choice )
    game = Game(player1, player2)
    return game.who_wins()





