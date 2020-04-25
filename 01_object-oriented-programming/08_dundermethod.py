class User:
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return f'The email for this user is {self.email}'

    def __len__(self):
        return len(self.email)

wizard = User('test@gmail.com')
print(wizard)
print(len(wizard))