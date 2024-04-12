class Dog:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # En funktion som hör till en klass är kallas för metod
    def bark(self):
        print(f"{self.name} barks")


dog1 = Dog("Golden Retriever", "Rolf")
dog2 = Dog("Bulldog", "Leif")
dog3 = Dog("Putbull", "Anna")

dog1.bark()


def summa(lista):
    total = 0
    for nummer in lista:
        total += nummer

    return total


a = [1, 2, 3]
print(summa(a))

1 + 2

a: int = 1
b: float = 1.1
c: complex = 1 + 1j
d: str = "1"
e: bool = True

text = "abcd"

i = 0
while i < len(text):
    täcken = text[i]
    print(täcken)
    i += 1


for täcken in text:
    print(täcken)

iterabel = (345, 3, 6.67, 2)
iterabel2 = [345, 3, 6.67, 2]
# for värde in iterabel:
#     print(värde)


for i in range(1, 5, 2):
    print(i)


from my_library import matte
from my_library import hjälpfunktioner

print(matte.PI)


# indata = input()
#
# if indata == str(5):
#     print("Indatan är nummret 5")
# else:
#     print("Indatan är INTE nummret 5")

int()
float()
str()
bool()
list()
tuple()
dict()

[1,2,3]
(1,2,3)

print(len("asdasdasd"))


kvot = 5 // 2
rest = 5 % 2

a = 1
b = 2
c = 3

if not (a == 1 and c > b):
    print(a, b, c)
elif c > a:
    print("j")
else:
    print("h")


print()


def


for i in range(5):
    print("a")

    if i == 3:
        continue

    print("b")

