"""room module containing Room class and methods"""

class Room():
    """Room class creates a room object"""

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def set_description(self, room_description):
        """sets the description of the room instance"""
        self.description = room_description

    def get_description(self):
        """gets the room instance description"""
        return self.description

    def describe(self):
        """print the room instance description to screen"""
        print(self.description)

    def set_name(self, room_name):
        """sets the room instance name"""
        self.name = room_name

    def get_name(self):
        """gets the room instance name"""
        return self.name

    def link_room(self, room_to_link, direction):
        """this method links room objects with a direction"""
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """displays the details of a room and the direction of linked rooms """
        print()
        # print()
        print(self.name)
        print('-' * 25)
        print(self.description)
        # print('-' * 25)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The ' + room.get_name() + ' is ' + direction)

    def move(self, direction):
        """references the room in direction given if available"""
        if direction in self.linked_rooms:
            # print(self.linked_rooms[direction].name)
            return self.linked_rooms[direction]
        print("You can't go that way")
        print()
        return self
