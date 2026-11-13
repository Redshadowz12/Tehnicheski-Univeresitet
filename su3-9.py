class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def sound(self):
        print("WOOF WOOF")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def sound(self):
        print("Meow")

dog1 = Dog("Rex", 3)
cat1 = Cat("Leo", 2)
dog1.sound()
cat1.sound()