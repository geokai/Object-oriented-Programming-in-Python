"""item module containing Item class and methods"""


class Item():
    """Item class creates an Item object"""

    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def set_name(self, item_name):
        """sets the item name"""
        self.name = item_name

    def get_name(self):
        """sets the item name"""
        return self.name

    def set_description(self, item_description):
        """sets the Item description"""
        self.description = item_description

    def get_description(self):
        """returns the Item description"""
        return self.description

    def find_item(self):
        """method to find item"""
        print('You found the {}!'.format(self.name))

    def use_item(self):
        """method to perform action with Item"""
        print('You are using the {}!'.format(self.name))


class Lantern(Item):
    """Lantern class"""

    # def __init__(self, item_name):
    #     super().__init__(self, item_name)


class Compass(Item):
    """Compass class"""

    # def __init__(self, item_name):
    #     super().__init__(self, item_name)
