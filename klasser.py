#Klassen för spelaren
class Player:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def is_alive(self):
        return self.hp > 0


#Klasser för fiender och dess subtyper
class Enemy:

    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def is_alive(self):
        return self.hp > 0

class Placeholder_Enemy1:
    def __init__(Enemy):
        super.__init__(name="Placeholder_Enemy1, hp=5, dmg=1")

class Placeholder_Enemy2:
    def __init__(Enemy):
        super.__init__(name="Placeholder_Enemy2, hp=10, dmg=3")

class Placeholder_Enemy3:
    def __init__(Enemy):
        super.__init__(name="Placeholder_Enemy3, hp=20, dmg=5")


#Klasser för föremål
class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class Placeholder_Item1:
    def __init__(self, amt):
        self.amt = amt
        super().__init__ (name="Placeholder_Item1",
          