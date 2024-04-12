l1 = [1, 2, 3, 16, 2, 100, 95, 21]

l2 = ["pelle", "melle"]

l3 = [True, 1.4, "pilot", 2]
#     0     1    2        3
#    -4    -3   -2       -1

#lista[start:stop:step]

# print(l3[::2])  # -> [True, "pilot"]
# print(l3[1:3])  # -> [1.4, "pilot"]

t2 = [(0, -1), ["ö1"], [0, -1]]


def func(a, b, c):
    return a + b + c

a = func(1, 2, 3)

print(a)


def str_to_nums(s):
    result = []
    for char in s:
        result.append(ord(char))

    return result


print(str_to_nums("hej"))
print(str_to_nums("annan sträng"))
