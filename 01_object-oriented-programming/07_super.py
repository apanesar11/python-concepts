class User:
    def __init__(self, email):
        self.email = email

class Wizard(User):
    def __init__(self, email, name, power):
        super().__init__(email)
        # another way to do this
        # User.__init__(self, email)
        self.name = name
        self.power = power

wizard = Wizard('test@gmail.com', 'wizard1', 5000)
print(wizard.email)