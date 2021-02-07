from flask import Flask, render_template, url_for, redirect
# from game.game import Game
from game.player import Player
from game.CreatePlayerForm import CreatePlayerForm
# from game.Field import Pawn
from game.Field import Field
from enum import Enum, auto

app = Flask(__name__)
# gra = Game()
# gracz = Player()

app.config['SECRET_KEY'] = '72a33ed0e644f52e31332903fea93374'

pionki = []
# class Player:
#     def __init__(self, name):
#         self.name = name
#         # self.score = 0
#         # self.myBoard = []
#     score = 0
#     colour_pawn = ''
#     current_fields = []

    # def move(self):
list_of_fields = []
# occupied_fields = []
number_of_fields = 1
@app.route('/home')
def hello_world():
    return 'Hello World'


# class Pawn:
#     def __init__(self, color, x, y):
#         self.color = color
#         self.x = x
#         self.y = y

@app.route('/player', methods=['GET', 'POST'])
def new_player():
    form = CreatePlayerForm()
    if form.validate_on_submit():

        global gracz1, gracz2, pionki, number_of_fields, field, list_of_fields
        # global gracz2
        gracz1 = Player(name=form.nick1.data)
        # gracz1.pawn = 'WHITE'
        gracz2 = Player(name=form.nick2.data)
        field1 = Field('white')
        field2 = Field('green')
        field3 = Field('black')
        # pionek = Pawn('white', 4, 5)
        # pionki = [pionek]
        # for x in range(1, number_of_fields+1):
        #     x = Field('green')
        list_of_fields = [field1, field2, field3]






        # pawn1 = Pawn('white', 4, 4)
        # pawn2 = Pawn('white', 5, 5)
        # pawn3 = Pawn('black', 4, 5)
        # pawn4 = Pawn('black', 5, 4)
        # list_of_pawns = [pawn1, pawn2, pawn3, pawn4]
        # occupied_fields = [pawn1, pawn2, pawn3, pawn4]
        # gracz2.pawn = 'BLACK'
        # gracz2 = Player(name=form.nick.data)
        # gracz2.colour_pawn = 'BLACK'

        return redirect(url_for('plansza'))
    return render_template('form.html', form=form)


@app.route('/plansza')
def plansza():
    # global gra
    return render_template('plansza.html', gracz1=gracz1, gracz2=gracz2, list_of_fields=list_of_fields)
#
# @app.route('/moveto/<rowID>/<columnID>')
# def Move(rowID,columnID):


# class FieldColour(Enum):
#     WHITE = auto()
#     BLACK = auto()
#     EMPTY = auto()
# @app.route('/move/<rowID>/<columnID>')
# def move(rowID, columnID, temporary=None):
#     temporary_board = []
#     if rowID and columnID ==


if __name__ == '__main__':
    app.run()
