class User:
    @staticmethod
    def login():
        print('you have successfully logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with {self.num_arrows} arrows')

class Hybrid(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)

    def attack(self):
        print(f'attacking with power of {self.power} and {self.num_arrows} arrows')

hybrid = Hybrid('Arashdeep', 5000, 10)
hybrid.attack()