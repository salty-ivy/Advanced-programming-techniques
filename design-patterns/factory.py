# the factory method and the abstract factory
# factory decouples the creation of object creation from object use
# abstract family is multiple factory methods creating objects of same family

class Frog:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self,obstacle):
        act = obstacle.act()
        msg = f"{self} the frog encounters {obstacle} and {act}!"
        print(msg)

class Bug:
    def __init__(self):
        return 'a bug'

    def action(self):
        return 'eats it'

# Abstract Factory
class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return "\n\n\t------Frog World------"

    def make_character(self):
        return Frog()

    def make_obstacle(self):
        return Bug()

class Wizard:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the frog encounters {obstacle} and {act}!"
        print(msg)

class Ork:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return "\n\n\t------Frog World------"

    def make_character(self):
        return Wizard()
    def make_obstacle(self):
        return Ork()

class GameEnvironmentt:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)
