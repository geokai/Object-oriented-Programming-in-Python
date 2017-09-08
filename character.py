"""character class module"""


class Character():
    """Character class"""

    characters = []
    num_of_chractrs = 0

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        Character.characters.append(self.name)
        Character.num_of_chractrs += 1

    # Describe this character
    def describe(self):
        """this method returns the instance description"""
        print()
        print(self.name + " is here!")
        print(self.description)
        print()

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """sets the converstation value of an instance"""
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """this method actions the instance conversation value"""
        if self.conversation is not None:
            print("[" + self.name + " says]:\n" + self.conversation)
            print()
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, *, combat_item=None):
        """this method return a bool"""
        if combat_item is None:     # ?..could also be, if not combat_item: ..?
            print(self.name + " doesn't want to fight with you.")
        else:
            print(self.name + " fights you with a " + combat_item + "!")


class Enemy(Character):
    """Enemy class inherits from Character"""

    def __init__(self, char_name, char_description, *, weapons=None):
        super().__init__(char_name, char_description)
        if weapons is None:
            self.weapons = []
        else:
            self.weapons = weapons

    def add_weapon(self, weapon):
        """method add a weapon item to the instances weapon list"""
        self.weapons.append(weapon)

    def get_weapons(self):
        """returns the weapons list of the instance"""
        return self.weapons
