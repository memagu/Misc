# conv = {" ": "0",
#         "a": "1",
#         "b": "2",
#         "c": "3",
#         "d": "4",
#         "e": "5",
#         "f": "6",
#         "g": "7",
#         "h": "8",
#         "i": "9",
#         "j": "10",
#         "k": "11",
#         "l": "12",
#         "m": "13",
#         "n": "14",
#         "o": "15",
#         "p": "16",
#         "q": "17",
#         "r": "18",
#         "s": "19",
#         "t": "20",
#         "u": "21",
#         "v": "22",
#         "w": "23",
#         "x": "24",
#         "y": "25",
#         "z": "26"}
#
# word = "create admin role"
# result = ""
# for char in word:
#     result += conv[char]
#
# print(result)


# def fib(n):
#     if n < 2:
#         return 1
#
#     return fib(n-1) + fib(n-2)
#
#
# # 1 1 2 3 5 8 13 21
#
#
# for i in range(10):
#     print(fib(i))

import math

num = 1
for i in range(1, 1_000_000_000):
    num += math.sin(i) / i
    num += math.sin(-i) / -i
    print(num, end="\r")

