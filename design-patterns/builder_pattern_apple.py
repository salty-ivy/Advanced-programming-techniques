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

class Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = (
                f'Memory: {self.memory}',
                f'Hard Disk: {self.hdd}',
                f'Graphics: {self.self.gpu}',
                )
        return '\n'.join(info)

### The builder

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount
    def configure_hdd(self, amount):
        self.computer.hdd = amount
    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model

###  The Director

class HardwareEngineer:
    def __init__(self):
        self.builder = None
    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        steps = (self.builder.configure_memory(memory),
                 self.builder.configure_hdd(hdd),
                 self.builder.configure_gpu(gpu),
            )
        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer


if __name__ == '__main__':
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu='Some GPU model')
    computer = engineer.computer
    print(computer)
    afac = AppleFactory()
    mc_mini = afac.build_computer(MINI14)
    print(mc_mini)

