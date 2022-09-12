"""
Int to roman
"""
num = "149"

integer_to_roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
index_to_builders = ((1, 5), (10, 50), (100, 500), 1000)

result = ""
for i, part in enumerate(num):
    i = (len(num) - 1 - i)
    part = int(part) * 10 ** i
    print(part)

    if part in integer_to_roman:
        result += integer_to_roman[part]
        continue

    if i > 2:
        result += part // 1000
        continue

    if part > index_to_builders[i][1]:
        if part == index_to_builders[i+1][0] - index_to_builders[i][0]:
            result += integer_to_roman[index_to_builders[i][0]] + integer_to_roman[index_to_builders[i+1][0]]
            continue
        result += integer_to_roman[index_to_builders[i][0]] * (part - index_to_builders[i][1])
        continue

    if part == index_to_builders[i][1] - index_to_builders[i][0]:
        result += integer_to_roman[index_to_builders[i][0]] + integer_to_roman[index_to_builders[i][1]]
        continue

    result += integer_to_roman[index_to_builders[i]] * part

print(result)
