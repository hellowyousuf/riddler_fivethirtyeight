import random

playdic = {'double': ['scissors', 'paper'],
           'scissors': ['paper'],
           'rock': ['scissors', 'double'],
           'paper': ['rock']
           }


class Player(object):
    def __init__(self):
        self.score = [0, 0]
        self.play = ''
        self.wins = 0

    def generator(self):
        self.play = playdic.keys()[random.randint(0, 3)]


def ronda(a, b):
    winner = None

    while winner is None:
        a.generator()
        b.generator()

        if a.play == b.play:
            pass
        elif a.play in playdic[b.play]:
            b.score[0] += 1
            a.score[1] += 1
            winner = b
            loser = a
        else:
            a.score[0] += 1
            b.score[1] += 1
            winner = a
            loser = b

    if winner.play == 'scissors':
        winner.score[0] += 1
        loser.score[1] += 1


def matchsim(a, b):
    a.score, b.score = [0, 0], [0, 0]
    while a.score[0] < 2 and b.score[0] < 2:
        ronda(a, b)
    if a.score[0] == 2:
        a.wins += 1
    else:
        b.wins += 1


pl1 = Player()
pl2 = Player()
