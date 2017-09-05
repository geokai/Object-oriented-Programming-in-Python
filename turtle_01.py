from turtle import Turtle
from random import randint

laura = Turtle()
laura.color('red', 'white')
laura.shape('turtle')
laura.penup()
laura.goto(-160, 100)
laura.pendown()

lauren = Turtle()
lauren.color('blue', 'white')
lauren.shape('turtle')
lauren.penup()
lauren.goto(-160, 70)
lauren.pendown()

rik = Turtle()
rik.color('green', 'white')
rik.shape('turtle')
rik.penup()
rik.goto(-160, 40)
rik.pendown()

carrieanne = Turtle()
carrieanne.color('black', 'white')
carrieanne.shape('turtle')
carrieanne.penup()
carrieanne.goto(-160, 10)
carrieanne.pendown()

for movement in range(100):
    laura.forward(randint(1, 5))
    lauren.forward(randint(1, 5))
    rik.forward(randint(1, 5))
    carrieanne.forward(randint(1, 5))

print('laura: \t\t{}'.format(laura.pos()[0]))
print('lauren: \t{}'.format(lauren.pos()[0]))
print('rik: \t\t{}'.format(rik.pos()[0]))
print('carrieanne: \t{}'.format(carrieanne.pos()[0]))
print('-' * 25)

win = max(laura.pos()[0], lauren.pos()[0], rik.pos()[0], carrieanne.pos()[0])

if win == laura.pos()[0]:
    winner = 'laura'
elif win == lauren.pos()[0]:
    winner = 'lauren'
elif win == rik.pos()[0]:
    winner = 'rik'
else:
    winner = 'carrieanne'


print('The winner is {}!'.format(winner))
print('-' * 25)
