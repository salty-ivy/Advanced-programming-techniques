# builder patter for python 
# Demo is based on apple factory 
# buulder is used to building complex objects whose build process comes in steps


MINI14 = '1.4 GHz Mac mini'

class AppleFactory:
    class McMini14:
        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = 'M2 chip grapihcs'

        def __str__(self):
            info = (f'Model: {MINI14}',
                    f'Memory: {self.memory}',
                    f'Hard Disk: {self.hdd}',
                    f'Graphics Card: {self.gpu}')
            return "\n".join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.McMini14()
        else:
            msg = f"I don't know how to build model: {model}"
            print(msg)


if __name__ == '__main__':
    afac = AppleFactory()
    mc_mini = afac.build_computer(MINI14)
    print(mc_mini)

