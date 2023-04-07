from turtle import *
from random import randint
from copy import deepcopy
import time
title('Solitaire')
screen = getscreen()
screen.screensize(512, 512)


class Card:
    def __init__(self, suit, number, hidden):
        self.suit = suit
        self.number = number
        self.color = 'red' if suit in ['H', 'D'] else 'black'
        self.hidden = hidden

    def __str__(self): return f"{self.suit}.{self.number}"

    def drawCard():
        begin_poly()
        for _ in range(2):
            forward(40)
            left(90)
            forward(20)
            left(90)
        end_poly()

        p = get_poly()
        register_shape('card', p)


suits = ['H', 'S', 'D', 'C']
numbers = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
allTheCards = []
for suit in suits:
    for number in numbers:
        myCard = Card(suit, number, False)
        allTheCards.append(myCard)

board = []
for i in range(7):
    stack = []
    for j in range(i):
        randomIndex = randint(0, len(allTheCards)-1)
        k2 = deepcopy(allTheCards[randomIndex])
        k2.hidden = j < i-1
        stack.append(k2)
        del allTheCards[randomIndex]
    board.append(stack)

clear()
tracer(0)
penup()
right(90)
x = -100

for stack in board:
    goto(x, 100)
    x += 30
    for card in stack:
        if card.hidden:
            color('#0010ff')
            write('***')
        else:
            if card.color == 'black':
                color('#000000')
            elif card.color == 'red':
                color('#ff0000')
            write(card)
        forward(20)

goto(150, 80)
color('#007710')
for _ in range(4):
    write('***')
    forward(30)

goto(-120, 80)
color('#007710')
write('***')
goto(-120, 50)

for _ in range(3):
    write('***')
    forward(10)

update()


def doSomething(x, y): print(x, y)


onscreenclick(doSomething)
mainloop()
