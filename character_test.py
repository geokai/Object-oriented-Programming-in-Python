"""test module for Character class object"""


from character import Character, Enemy


# create friendly character:
katrina = Character('Katrina', "I'm Katrina, your friendly, skeletal zombie!")
# call the 'describe' method on the Character object:
katrina.describe()

# create a Enemy object:
dave = Enemy('Dave', 'A rotten zombie')
# call the 'describe' method on the Enemy object:
dave.describe()

# create a converstation with object:
# dave.set_conversation("Hello, my name's Dave.\nI'm a rotten zombie!")

# dave.talk()

# fight dave with a combat_item(kwarg):
# dave.fight(combat_item='wet kipper')

# fight dave with nothing:
# dave.fight()
