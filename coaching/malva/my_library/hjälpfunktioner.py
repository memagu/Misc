def printa_två_gånger(objekt):
    print(objekt)
    print(objekt)


def summa(iterabel):
    total = 0
    for nummer in iterabel:
        total += nummer

    return total


def all_true(iterable):
    for object in iterable:
        if not bool(object):
            return False

    return True


a = 1


def global_example():
    global a
    a += 1


print(a)
global_example()
print(a)

b = ["x", "y", "z"]
# c = b.pop(0)
# b.append(6)
# b.insert(1, 88)
print(b[2])

# print(b, c)


g = {
    "namn": "pelle",
    "ålder": 18
}


# print(g["pelle"])


# int("pepperoni")

# def funktionsnamn(argument1, argument2, ...):
#     vad
#     den
#     ska
#     göra
#     ...

a = (
    (1, 2),
    (3, 4),
    (5, 6)
)


print(dict(a))

print(tuple("asdjhakjsd"))
print(list("asdjhakjsd"))

a = ["x", "z", "y"]
b = sorted(a)
print(a, b)
a.sort()
print(a)


for key, value in g.items():
    print(f"nyckel={key} och värde={value}")



a = [1, 2, 3]
a.extend("hej")

print(a)