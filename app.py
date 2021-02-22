from flask import Flask, render_template, url_for, redirect
from game.CreatePlayerForm import CreatePlayerForm


app = Flask(__name__)

current_player = 1
koniec_gry = False
remis = False
app.config['SECRET_KEY'] = '72a33ed0e644f52e31332903fea93374'


class Player:
    global current_player

    def __init__(self, name):
        self.name = name
        self.field = []
        self.score = 2
        self.win = False

    def move(self, x, y, second_player):
        global current_player, koniec_gry, remis

        x = int(x)
        y = int(y)
        poczatkowy_x = x
        poczatkowy_y = y
        cant_move = []

# !---------------------            W PRAWO            ------------------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:     #sprawdz, czy mozna tu stanac (puste pole)
            temporary_fields = []

            y += 1                                                                     # sprawdz pole po PRAWEJ

            if [x, y] not in self.field and [x, y] not in second_player.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            elif[x, y] in self.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            else:
                while [x, y] in second_player.field:                                      #dopoki pole po prawej to pionek przeciwnika
                    temporary_fields.append([x, y])                                        #dodawaj takie pole do tymczasowej tablicy
                    y += 1
                if [x, y] in self.field:                                                  #jesli trafisz na swoj pionek
                    for field in temporary_fields:
                        second_player.field.remove(field)
                        if field not in self.field:                                 #to zakoncz ruch i pododawaj/pousuwaj do tablicy
                            self.field.append(field)
                if [x, y] not in self.field and [x, y] not in second_player.field:
                    cant_move.append([poczatkowy_x, poczatkowy_y])

            y = poczatkowy_y                                               #i wroc sie do poczatku

#     !--------------------      W GÓRE         -------------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []

            x -= 1   #w góre
            if [x, y] not in self.field and [x, y] not in second_player.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            elif [x, y] in self.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            else:
                while [x, y] in second_player.field:  # dopoki pole po prawej to pionek przeciwnika
                    temporary_fields.append([x, y])
                    x -= 1
                if [x, y] in self.field:
                    for field in temporary_fields:
                        second_player.field.remove(field)
                        if field not in self.field:
                            self.field.append(field)
                if [x, y] not in self.field and [x, y] not in second_player.field:
                    cant_move.append([poczatkowy_x, poczatkowy_y])

            x = poczatkowy_x


        # !--------------          W DÓŁ         --------------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []

            x += 1

            if [x, y] not in self.field and [x, y] not in second_player.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            elif [x, y] in self.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            else:
                while [x, y] in second_player.field:
                    temporary_fields.append([x, y])
                    x += 1
                if [x, y] in self.field:
                    for field in temporary_fields:
                        second_player.field.remove(field)
                        if field not in self.field:
                            self.field.append(field)
                if [x, y] not in self.field and [x, y] not in second_player.field:
                    cant_move.append([poczatkowy_x, poczatkowy_y])

            x = poczatkowy_x


# !---------------         W LEWO         ---------------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []

            y -= 1

            if [x, y] not in self.field and [x, y] not in second_player.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            elif [x, y] in self.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            else:
                while [x, y] in second_player.field:
                    temporary_fields.append([x, y])
                    y -= 1
                if [x, y] in self.field:
                    for field in temporary_fields:
                        second_player.field.remove(field)
                        if field not in self.field:
                            self.field.append(field)
                if [x, y] not in self.field and [x, y] not in second_player.field:
                    cant_move.append([poczatkowy_x, poczatkowy_y])

            y = poczatkowy_y


# !---------        SKOS PRAWO GÓRA             ------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []

            x -= 1
            y += 1

            if [x, y] not in self.field and [x, y] not in second_player.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            elif [x, y] in self.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            else:
                while [x, y] in second_player.field:
                    temporary_fields.append([x, y])
                    x -= 1
                    y += 1
                if [x, y] in self.field:
                    for field in temporary_fields:
                        second_player.field.remove(field)
                        if field not in self.field:
                            self.field.append(field)
                if [x, y] not in self.field and [x, y] not in second_player.field:
                    cant_move.append([poczatkowy_x, poczatkowy_y])

            x = poczatkowy_x
            y = poczatkowy_y


# !--------             SKOS LEWO GÓRA          ------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []

            x -= 1
            y -= 1

            if [x, y] not in self.field and [x, y] not in second_player.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            elif [x, y] in self.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            else:
                while [x, y] in second_player.field:
                    temporary_fields.append([x, y])
                    x -= 1
                    y -= 1
                if [x, y] in self.field:
                    for field in temporary_fields:
                        second_player.field.remove(field)
                        if field not in self.field:
                            self.field.append(field)
                if [x, y] not in self.field and [x, y] not in second_player.field:
                    cant_move.append([poczatkowy_x, poczatkowy_y])

            x = poczatkowy_x
            y = poczatkowy_y


# !-------------        SKOS PRAWO DÓŁ         ----------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []

            x += 1
            y += 1

            if [x, y] not in self.field and [x, y] not in second_player.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            elif [x, y] in self.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            else:
                while [x, y] in second_player.field:
                    temporary_fields.append([x, y])
                    x += 1
                    y += 1
                if [x, y] in self.field:
                    for field in temporary_fields:
                        second_player.field.remove(field)
                        if field not in self.field:
                            self.field.append(field)
                if [x, y] not in self.field and [x, y] not in second_player.field:
                    cant_move.append([poczatkowy_x, poczatkowy_y])

            x = poczatkowy_x
            y = poczatkowy_y




# !---------               SKOS LEWO DÓŁ             ----------------!

        if [x, y] not in self.field and [x, y] not in second_player.field:
            temporary_fields = []

            x += 1
            y -= 1

            if [x, y] not in self.field and [x, y] not in second_player.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            elif [x, y] in self.field:
                cant_move.append([poczatkowy_x, poczatkowy_y])
            else:
                while [x, y] in second_player.field:
                    temporary_fields.append([x, y])
                    x += 1
                    y -= 1
                if [x, y] in self.field:
                    for field in temporary_fields:
                        second_player.field.remove(field)
                        if field not in self.field:
                            self.field.append(field)
                if [x, y] not in self.field and [x, y] not in second_player.field:
                    cant_move.append([poczatkowy_x, poczatkowy_y])

            x = poczatkowy_x
            y = poczatkowy_y
            if len(cant_move) != 8:
                self.field.append([poczatkowy_x, poczatkowy_y])
            else:
                pass
        current_player *= -1

        self.score = len(self.field)
        second_player.score = len(second_player.field)


# @app.route('/home')
# def home():
#     return render_template('basic.html')


@app.route('/player', methods=['GET', 'POST'])
def new_player():
    form = CreatePlayerForm()
    if form.validate_on_submit():

        global gracz_bialy, gracz_czarny

        gracz_bialy = Player(name=form.nick1.data)
        # gracz_bialy.field.append([2, 4])
        # gracz_bialy.field.append([4, 3])
        # gracz_bialy.field.append([3, 6])
        # gracz_bialy.field.append([3, 4])
        gracz_bialy.field.append([4, 4])
        # gracz_bialy.field.append([4, 5])
        # gracz_bialy.field.append([4, 6])
        # gracz_bialy.field.append([4, 7])
        gracz_bialy.field.append([5, 5])
        # gracz_bialy.score = 2
        # gracz_bialy.field.append([5, 6])
        # gracz_bialy.field.append([6, 2])
        # gracz_bialy.field.append([6, 4])
        # gracz_bialy.field.append([6, 6])
        # gracz_bialy.field.append([6, 5])
        # gracz_bialy.field.append([6, 7])
        # gracz_bialy.field.append([7, 4])
        # gracz_bialy.field.append([7, 6])
        # gracz_bialy.field.append([8, 4])
        gracz_czarny = Player(name=form.nick2.data)
        # gracz_czarny.field.append([3, 6])
        # gracz_czarny.field.append([3, 4])
        gracz_czarny.field.append([4, 5])
        # gracz_czarny.field.append([4, 6])
        gracz_czarny.field.append([5, 4])
        # gracz_czarny.field.append([5, 6])
        # gracz_czarny.score = 2
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
    global koniec_gry

    if current_player == 1:
        gracz_bialy.move(rowID, columnID, gracz_czarny)
        if gracz_bialy.score + gracz_czarny.score == 64 or gracz_bialy.score == 0 or gracz_czarny.score == 0:
            return redirect(url_for('end_game'))

        return redirect(url_for('plansza', current_player=current_player))

    else:
        gracz_czarny.move(rowID, columnID, gracz_bialy)
        if gracz_bialy.score + gracz_czarny.score == 64 or gracz_bialy.score == 0 or gracz_czarny.score == 0:
            return redirect(url_for('end_game'))
        return redirect(url_for('plansza', current_player=current_player))

@app.route('/koniec_gry')
def end_game():
    global winner

    if gracz_bialy.score > gracz_czarny.score:
        winner = gracz_bialy.name
    elif gracz_bialy.score < gracz_czarny.score:
        winner = gracz_czarny.name
    elif gracz_bialy.score == gracz_czarny.score:
        winner = 'remis'
    return render_template('koniec_gry.html', winner=winner)


# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5181, debug=True)


