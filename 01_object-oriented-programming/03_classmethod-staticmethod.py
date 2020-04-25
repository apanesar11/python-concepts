class Person:
    is_real = True
    def __init__(self, name="anonymous", age=0):
        if Person.is_real:
            self.name = name
            self.age = age

    @staticmethod
    def hello1(user):
        print(f'staticmethod Hello {user}')

    @classmethod
    def hello2(cls, user):
        print(f'classmethod Hello {user}')

    @classmethod
    def generate_cool_person(cls):
        return cls('Cool Person', 100)


Person.hello1('Frank')
Person.hello2('Frank')
cool_person = Person.generate_cool_person()
print(cool_person.name)