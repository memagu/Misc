while True:
    s = input().split()

    a = int(s[0])
    b = int(s[2])
    t = s[1]

    if t == "+":
        print(a + b)

    elif t == "-":
        print(a - b)

    elif t == "/":
        print(a / b)

    elif t == "*":
        print(a * b)

    elif t == "**" or t == "^":
        print(a ** b)

    elif t == "%":
        print(a % b)

    else:
        exit()

