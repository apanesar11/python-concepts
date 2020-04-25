class Person:
    is_real = True

    def __init__(self, name, age):
        if Person.is_real:
            self.name = name
            self.age = age

    def hello(self, user):
        print(f'Hello {user}, my name is {self.name}')


person1 = Person('Arashdeep', 20)
print(person1.name)
print(person1.age)
person1.hello('Frank')