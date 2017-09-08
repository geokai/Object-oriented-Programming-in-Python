"""test module for Character class object"""


from character import Character


# create a Character object:
dave = Character('Dave', 'A rotten zombie')

# call the 'describe' method on the object:
dave.describe()

# create a converstation with object:
dave.set_conversation("Hello, my name's Dave.\nI'm a rotten zombie!")

dave.talk()

# fight dave with a combat_item(kwarg):
dave.fight(combat_item='wet kipper')

# fight dave with nothing:
ave.fight()
