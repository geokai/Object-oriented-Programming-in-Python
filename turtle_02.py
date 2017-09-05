"""Generate 'turtles' from the Turtle module and race them"""

from turtle import Turtle
from random import randint


TURTLES = []
TURTLE_COLORS = ('red', 'blue', 'green', 'black')
PLAYERS = []

# initial 'neighbouring' position of each turtle:
vPos = 100

# create the turtle objects form the 'Turtle' class according to the
# 'TURTLE_COLORS' list:
for trtl_col in TURTLE_COLORS:
    trtl = Turtle()
    trtl.color(trtl_col)
    trtl.shape('turtle')
    trtl.penup()
    trtl.goto(-160, vPos)
    trtl.pendown()

    # decrement the neighbouring position of each turtle by 30 each time
    # through the loop:
    vPos -= 30

    # append each created object to the 'TURTLES' list:
    TURTLES.append(trtl)

# assign each turtle object to a name variable & append to the 'PLAYERS' list:
# (this only serves to help reset the canvas form the cli using a loop - debug)
laura = TURTLES[0]
PLAYERS.append(laura)
rik = TURTLES[1]
PLAYERS.append(rik)
lauren = TURTLES[2]
PLAYERS.append(lauren)
carrieanne = TURTLES[3]
PLAYERS.append(carrieanne)


# run the race using the 'randint' random generator for the 'forward' direction
# for each turtle by way of loop:
for movement in range(100):
    laura.forward(randint(1, 5))
    rik.forward(randint(1, 5))
    lauren.forward(randint(1, 5))
    carrieanne.forward(randint(1, 5))

# print the final positions of each racer:
print('-' * 25)
print('laura: \t\t{}'.format(laura.pos()[0]))
print('rik: \t\t{}'.format(rik.pos()[0]))
print('lauren: \t{}'.format(lauren.pos()[0]))
print('carrieanne: \t{}'.format(carrieanne.pos()[0]))
print('-' * 25)

# check for the highest final position value using the 'max' function:
win = max(laura.pos()[0], rik.pos()[0], lauren.pos()[0], carrieanne.pos()[0])

# test for the value of 'win' and assign the coresponding name to 'winner':
if win == laura.pos()[0]:
    winner = 'laura'
elif win == rik.pos()[0]:
    winner = 'rik'
elif win == lauren.pos()[0]:
    winner = 'lauren'
else:
    winner = 'carrieanne'


# print the winning turtle according to the 'winner' name value:
print('The winner is {}!'.format(winner))
print('-' * 25)
