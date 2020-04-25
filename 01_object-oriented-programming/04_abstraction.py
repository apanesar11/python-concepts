class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def greeting(self):
        print(f'Hello, my name is {self._name} and I am {self._age} years old.')

person1 = Person('Arashdeep', 20)
person1.greeting()
person1.name = 'cool'
person1.age = 100
person1.greeting()