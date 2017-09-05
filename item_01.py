"""item module containing Item class and methods"""


class Item():
    """Item class creates an Item object"""

    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def set_description(self, item_description):
        """sets the Item description"""
        self.description = item_description

    def get_description(self):
        """returns the Item description"""
        return self.description

    def use_item(self):
        """method to perform action with Item"""
        pass


class Lantern(Item):
    """Lantern class"""

    def __init__(self, item_name):
        super().__init__(self, item_name)


class Compass(Item):
    """Compass class"""

    def __init__(self, item_name):
        super().__init__(self, item_name)
