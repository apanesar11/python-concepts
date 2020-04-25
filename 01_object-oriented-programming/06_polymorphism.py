class User:
    @staticmethod
    def login():
        print('you have successfully logged in')

    @staticmethod
    def attack():
        print('preparing to attack')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack()
        print(f'attacking with power of {self.power}')

wizard = Wizard('wizard1', 5000)
wizard.attack()