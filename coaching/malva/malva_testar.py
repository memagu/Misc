"""
Gör en funktion som heter 'only_contains' och som tar två strängar som input, låt oss kalla dem 'a' och 'b'.
Funktionen ska returnera längden på 'a' om varje täcken i 'a' är 'b', annars returnera värdet -1

Exempel:
a="aaaaaa"
b="a"
svar: 6

a="aaaaab"
b="a"
svar: -1

"""


def only_contains(a, b):
    for char in a:
        if char != b:
            return -1

    return len(a)



"""
a = [1, 2, 3, 4, 5]
i = 0
while i < len(a):
    print(a[i])
    i += 1
"""
["value", ...]
("value", ...)
{"key": "value", ....}
TypeError
NameError
IndexError
KeyError
SyntaxError