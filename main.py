from turtle import *
from random import randint
from copy import deepcopy
import time

title("Solitaire")
screen = getscreen()
screen.screensize(512, 512)


#
# Our Card class
#
class Card:
    # Our card has a suit, a number, and can be hidden or shown.
    def __init__(self, suit, number, hidden):  # Card constructor
        self.suit = suit
        self.number = number

        # Hearts and diamonds are red
        if suit == 'H' or suit == 'D':
            self.color = 'red'
        else:
            self.color = 'black'

        self.hidden = hidden

    def __str__(self):  # String format
        return f"{self.suit}.{self.number}"

    def drawCard():  # Draw a card
        begin_poly()  # Begin the polygon
        for i in range(2):  # Draw the card
            forward(40)
            left(90)
            forward(20)
            left(90)
        end_poly()  # End the polygon

        p = get_poly()  # Get drawn polygon
        register_shape("card", p)  # Draw polygon


suits = ['H', 'S', 'D', 'C']
numbers = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

# All the possible cards in the game
allTheCards = []
for suit in suits:
    for number in numbers:
        myCard = Card(suit, number, False)
        allTheCards.append(myCard)

# Initialise the board
board = []
"""
for suit in suits:
    stack = []
    for number in numbers:
        stack.append(Card(suit, number, False))
    board.append(stack)
"""

# Add cards to board
for i in range(7):
    stack = []
    for j in range(i):
        randomIndex = randint(0, len(allTheCards) - 1)
        k2 = deepcopy(allTheCards[randomIndex])
        if (j < i - 1):
            k2.hidden = True
        else:
            k2.hidden = False
        stack.append(k2)
        del allTheCards[randomIndex]
    board.append(stack)

#
# Render Cards
#
clear()
tracer(0)
penup()
right(90)

# Render the board
x = -100
for stack in board:
    goto(x, 100)
    x += 30

    for card in stack:
        if card.hidden:
            color('#0010ff')
            write('***')
        else:
            if card.color == 'red':
                color('#ff0000')
            if card.color == 'black':
                color('#000000')

            write(card)

        forward(20)

# Render slots on right
goto(150, 80)
color('#007710')
for i in range(4):
    write('***')
    forward(30)

# Render the deck
goto(-120, 80)
color('#007710')
write('***')

goto(-120, 50)
for i in range(3):
    write('***')
    forward(10)

update()


def doSomething(x, y):
    print(x, y)


onscreenclick(doSomething)

# Starts event loop (calling Tkinter’s mainloop function.)
# Must be the last statement in a turtle graphics program.
mainloop()
