class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def kill(self):
        del self

    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        return self.age + other.age

dog = Dog("peter", 94)
dog2 = Dog("anders", 4)

print(repr(dog))
print(dog)

print(dog + dog2)



