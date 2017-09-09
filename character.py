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
        """this method prints a message form a Character instance"""
        _ = combat_item
        print(self.name + " doesn't want to fight with you.")


class Enemy(Character):
    """Enemy class inherits from Character"""

    def __init__(self, char_name, char_description, *, weapon=None):
        super().__init__(char_name, char_description)
        if weapon is None:
            self.weapon = None
        else:
            self.weapon = weapon
        self.weakness = None

    def set_weapon(self, weapon):
        """method add a weapon item to the instances object"""
        self.weapon = weapon

    def get_weapon(self):
        """returns the weapon value of the instance"""
        if self.weapon is None:
            print(self.name + ' has no weapons, make the most of it!!')
        else:
            return self.weapon

    def set_weakness(self, weakness_item):
        """set the weakness item"""
        self.weakness = weakness_item

    def get_weakness(self):
        """returns wekness item"""
        if self.weakness is None:
            print(self.name + ' has no weaknesses, BEWARE!!')
        else:
            print(self.name + "s' weakness is " + self.weakness)

    def fight(self, *, combat_item=None):
        """fight method override"""
        if combat_item == self.weakness:
            print('You fend ' + self.name + ' off with ' + combat_item + '!')
        elif combat_item == self.weapon:
            print(self.name + ' has ' + combat_item + ' too!')
            print("It's a draw.")
        else:
            print('Ha! ' + combat_item + ' does nothing against ' + \
                    self.name + '.')
            print(self.name + ' crushes you with ' + self.weapon + \
                    ', puny adventurer!!')
