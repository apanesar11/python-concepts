class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print('hello')


person1 = Person('Arashdeep', 20)
print(person1.name)
print(person1.age)
person1.hello()