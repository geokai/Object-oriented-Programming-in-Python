"""run file"""

from room_01 import Room

def main():
    kitchen = Room('Kitchen')
    dining_hall = Room('Dining Hall')
    ballroom = Room('Ballroom')


    kitchen.set_description('A dark, dank and mouldy room...!')
    dining_hall.set_description('Dark mahogany panelled walls, lit by candelabras.')
    ballroom.set_description('High, ornate ceilings with huge crystal chandeliers.')

    kitchen.link_room(dining_hall, 'south')
    dining_hall.link_room(kitchen, 'north')
    dining_hall.link_room(ballroom, 'west')
    ballroom.link_room(dining_hall, 'east')


    # game set-up:
    current_room = kitchen

    # game play loop:
    while True:
        print()
        current_room.get_details()
        command = input('> ')
        current_room = current_room.move(command)


if __name__ == '__main__':
    main()


# debug code below here:

# kitchen.get_details()
# dining_hall.get_details()
# ballroom.get_details()

# kitchen.get_description()
# kitchen.describe()
