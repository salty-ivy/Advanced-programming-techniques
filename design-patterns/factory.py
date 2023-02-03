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
        return Frog(self.player_name)

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
    def __str__(self):
        return 'an evil ork'
    def action(self):
        return 'kills it'

class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return "\n\n\t------Frog World------"

    def make_character(self):
        return Wizard(self.player_name)
    def make_obstacle(self):
        return Ork()

class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    try:
        age = int(input(f"welcome {name}. How old are you?"))
    except ValueError as e:
        print(f"Age {age} is invalid please try again...")
        return (False, age)
    return (True, age)

def main():
    name = input(f"Welcome. input your name")
    valid_name = False

    while not valid_name:
        valid_name, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play

if __name__=='__main__':
    main()
