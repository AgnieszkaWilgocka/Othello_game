from flask import Flask, render_template, url_for, redirect
# from game.game import Game
# from ..game.player import Player
# from game.player import Player
from game.CreatePlayerForm import CreatePlayerForm
# from game.Field import Pawn
# from game.Field import Field
from enum import Enum, auto

app = Flask(__name__)
# gra = Game()
# gracz = Player()
current_player = 1

app.config['SECRET_KEY'] = '72a33ed0e644f52e31332903fea93374'
class Player:
    global current_player
    def __init__(self, name):
        self.name = name
        self.field = []
        self.score = 0
        # self.current_player = 1


    def move(self, x, y, second_player):
        global current_player
        wykonano_ruch = 0
        x = int(x)
        y = int(y)
        puste_pole = bool
        # temporary_field = []
        # temporary_field_to_remove = []
        poczatkowy_x = x
        poczatkowy_y = y
        # print(int(x), int(y))

# !---------------------            W PRAWO            ------------------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:     #sprawdz, czy mozna tu stanac (puste pole)
            temporary_fields = []
            # temporary_fields.append([x, y])

            y += 1                                                                     # sprawdz pole po PRAWEJ

            while [x, y] in second_player.field:                                      #dopoki pole po prawej to pionek przeciwnika
                temporary_fields.append([x, y])                                        #dodawaj takie pole do tymczasowych tablic
                # temporary_field_to_remove.append([x, y])
                y += 1
                # wykonano_ruch = 1              #i przesuwaj sie w tym samym kierunku
            # if [x, y] not in self.field and [x, y] not in second_player.field:
            #     y = poczatkowy_y
            if [x, y] in self.field:                                                  #jesli trafisz na swoj pionek
                for field in temporary_fields:
                    second_player.field.remove(field)
                    if field not in self.field:                                 #to zakoncz ruch i pododawaj do tablic
                        self.field.append(field)
                # wykonano_ruch = 1
            y = poczatkowy_y

            #i wroc sie do poczatku
            # self.field.append([x, y])
            # puste_pole = True

#     !--------------------      W GÓRE         -------------------!
        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []
            # temporary_fields.append([x, y])

            x -= 1   #w góre

            while [x, y] in second_player.field:
                temporary_fields.append([x, y])
                    # temporary_field_to_remove.append([int(x), int(y)])
                x -= 1
                # wykonano_ruch = 1
            # if [x, y] not in self.field and [x, y] not in second_player.field:
            #     x = poczatkowy_x
            if [x, y] in self.field:
                                                        # if [int(x), int(y)] in self.field:
                for field in temporary_fields:
                    second_player.field.remove(field)
                    if field not in self.field:
                        self.field.append(field)
                    # for fields in temporary_field_to_remove:
                    #     second_player.field.remove(fields)
                    # temporary_field = []
                    # temporary_field_to_remove = []
                # wykonano_ruch = 1
            x = poczatkowy_x

            # current_player *= -1

        # !--------------          W DÓŁ         --------------------!
        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []
            # temporary_fields.append([x, y])

            x += 1

            while [x, y] in second_player.field:
                temporary_fields.append([x, y])
                x += 1
                # wykonano_ruch = 1
            if [x, y] in self.field:
                for field in temporary_fields:
                    second_player.field.remove(field)
                    if field not in self.field:
                        self.field.append(field)
                # wykonano_ruch = 1
            x = poczatkowy_x


# !---------------         W LEWO         ---------------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []
            # temporary_fields.append([x, y])

            y -= 1

            while [x, y] in second_player.field:
                temporary_fields.append([x, y])
                y -= 1
                # wykonano_ruch = 1

            if [x, y] in self.field:
                for field in temporary_fields:
                    second_player.field.remove(field)
                    if field not in self.field:
                        self.field.append(field)
                # wykonano_ruch = 1
            y = poczatkowy_y

        # if wykonano_ruch == 1:
        #     self.field.append([x, y])
        #     current_player *= -1
        # else:
        #     current_player *= -1

# !---------        SKOS PRAWO GÓRA             ------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []
            # temporary_fields.append([x, y])

            x -= 1
            y += 1

            while [x, y] in second_player.field:
                temporary_fields.append([x, y])

                x -= 1
                y += 1
                # wykonano_ruch = 1
            if [x, y] in self.field:
                for field in temporary_fields:
                    second_player.field.remove(field)
                    if field not in self.field:
                        self.field.append(field)
                # wykonano_ruch = 1
            x = poczatkowy_x
            y = poczatkowy_y

        # if wykonano_ruch == 1:
        #     self.field.append([x, y])
        #     current_player *= -1
        # else:
        #     current_player *= -1
# !--------             SKOS LEWO GÓRA          ------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []
            # temporary_fields.append([x, y])

            x -= 1
            y -= 1

            while [x, y] in second_player.field:
                temporary_fields.append([x, y])

                x -= 1
                y -= 1
                # wykonano_ruch = 1

            if [x, y] in self.field:
                for field in temporary_fields:
                    second_player.field.remove(field)
                    if field not in self.field:
                        self.field.append(field)
                # wykonano_ruch = 1
            x = poczatkowy_x
            y = poczatkowy_y
            # self.field.append([x, y])
            # current_player *= -1


# !-------------        SKOS PRAWO DÓŁ         ----------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []
            # temporary_fields.append([x, y])

            x += 1
            y += 1

            while [x, y] in second_player.field:
                temporary_fields.append([x, y])

                x += 1
                y += 1

            if [x, y] in self.field:
                for field in temporary_fields:
                    second_player.field.remove(field)
                    if field not in self.field:
                        self.field.append(field)
            x = poczatkowy_x
            y = poczatkowy_y
        # current_player *= -1
# !---------               SKOS LEWO DÓŁ             ----------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []
            # temporary_fields.append([x, y])

            x += 1
            y -= 1

            while [x, y] in second_player.field:
                temporary_fields.append([x, y])

                x += 1
                y -= 1

            if [x, y] in self.field:
                for field in temporary_fields:
                    second_player.field.remove(field)
                    if field not in self.field:
                        self.field.append(field)
            x = poczatkowy_x
            y = poczatkowy_y
        current_player *= -1
        # if wykonano_ruch == 1:
        #     self.field.append([x, y])
        #     current_player *= -1
        # else:
        #     current_player *= -1

#         !--------------          W DÓŁ         --------------------!
#         if [x, y] not in self.field and [x, y] not in second_player.field:
#             temporary_fields = []
#             x += 1
#
#             while [x, y] in second_player.field:
#                 temporary_fields.append([x, y])
#                 x  += 1
#
#             if [x, y] in self.field:
#                 for field in temporary_fields:
#                     second_player.field.remove(field)
#                     if field not in self.field:
#                         self.field.append(field)

        # if [int(x), int(y)] not in self.field and [int(x), int(y)] not in second_player.field:
        #     temporary_field.append([int(x), int(y)])
        #     x = int(x) + 1  # w dół
        #
        #     if [int(x), int(y)] not in self.field and [int(x), int(y)] not in second_player.field:
        #         x = int(x) - 1
        #
        #     elif [int(x), int(y)] in self.field:
        #         x = int(x) - 1
        #     else:
        #         while [int(x), int(y)] in second_player.field:
        #             temporary_field.append([int(x), int(y)])
        #             temporary_field_to_remove.append([int(x), int(y)])
        #             x = int(x) + 1
        #         if [int(x), int(y)] in self.field:
        #             for field in temporary_field:
        #                 if field not in self.field:
        #                     self.field.append(field)
        #             for fields in temporary_field_to_remove:
        #                 second_player.field.remove(fields)
        #         # else:
        #         #     pass
        #     # current_player *= (-1)
        # else:
        #     current_player *= (-1)
        #     pass


@app.route('/home')
def hello_world():
    return 'Hello World'


@app.route('/player', methods=['GET', 'POST'])
def new_player():
    form = CreatePlayerForm()
    if form.validate_on_submit():

        global gracz_bialy, gracz_czarny

        gracz_bialy = Player(name=form.nick1.data)
        # gracz_bialy.field.append([4, 3])
        # gracz_bialy.field.append([3, 6])
        gracz_bialy.field.append([4, 4])
        # gracz_bialy.field.append([4, 5])
        gracz_bialy.field.append([5, 5])
        # gracz_bialy.field.append([5, 6])
        # gracz_bialy.field.append([6, 2])
        # gracz_bialy.field.append([6, 6])
        # gracz_bialy.field.append([6, 5])
        # gracz_bialy.field.append([6, 7])
        # gracz_bialy.field.append([7, 4])
        # gracz_bialy.field.append([7, 6])
        # gracz_bialy.field.append([8, 4])
        gracz_czarny = Player(name=form.nick2.data)
        # gracz_czarny.field.append([3, 6])
        gracz_czarny.field.append([4, 5])
        gracz_czarny.field.append([5, 4])
        # gracz_czarny.field.append([6, 2])
        # gracz_czarny.field.append([8, 3])
        # gracz_czarny.field.append([8, 7])
        # gracz_czarny.field.append([6, 5])
        # gracz_czarny.field.append([6, 6])
        # gracz_czarny.field.append([7, 4])
        # gracz_czarny.field.append([6, 7])
        # gracz_czarny.field.append([6, 3])
        # gracz_czarny.field.append([6, 4])


        return redirect(url_for('plansza'))
    return render_template('form.html', form=form)

@app.route('/plansza')
def plansza():
    return render_template('plansza.html', gracz_bialy=gracz_bialy, gracz_czarny=gracz_czarny, current_player=current_player)



@app.route('/moveto/<rowID>/<columnID>')
def move(rowID, columnID):
    global current_player

    if current_player == 1:
        gracz_bialy.move(rowID, columnID, gracz_czarny)
        return redirect(url_for('plansza', current_player=current_player))
    else:
        gracz_czarny.move(rowID, columnID, gracz_bialy)
        return redirect(url_for('plansza', current_player=current_player))


if __name__ == '__main__':
    app.run()

