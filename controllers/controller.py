from flask import render_template
from app import app
from models.game import Game
from models.player import Player



@app.route('/home')
def index():
    return render_template('base.html')

# This line defines the URL route. 
@app.route('/<player1_choice>/<player2_choice>')
# As the class is only connected through the above the who_wins requires invoking on the game. This part
# is where the game is "defined" with the writen code. Player and Game classes are given the variables here. 
def rock_paper_scissors(player1_choice, player2_choice):
    player1 = Player("Stanley Kubrick", player1_choice)
    player2 = Player("Taika Waititi", player2_choice )
    game = Game(player1, player2)
    return render_template('result.html', result= game.who_wins())





