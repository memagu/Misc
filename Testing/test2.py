def go21(nums, target=21):
    operations = ['*', '+', '-', '/']
    parenthesis = [['', '', '', '', '', '', '', '', '', ''],
                   ['', '', '', '(', '', '', ')', '', '', ''],
                   ['', '(', '', '(', '', '', ')', ')', '', ''],
                   ['', '', '(', '(', '', '', ')', '', ')', ''],
                   ['', '(', '', '', ')', '', '', '', '', ''],
                   ['(', '(', '', '', ')', '', ')', '', '', ''],
                   ['', '', '', '', '', '(', '', '', ')', ''],
                   ['', '', '', '(', '', '(', '', '', ')', ')'],
                   ['', '(', '', '', ')', '(', '', '', ')', '']]

    # 0 | n + n + n + n
    # n | n + (n + n) + n
    # 2 | (n + (n + n)) + n
    # 3 | n + ((n + n) + n)
    # 4 | (n + n) + n + n
    # 5 | ((n + n) + n) + n
    # 6 | n + n + (n + n)
    # 7 | n + (n + (n + n))
    # 8 | (n + n) + (n + n)

    for a in operations:
        for b in operations:
            for c in operations:

                for i in range(4):
                    for j in range(4):
                        if j == i:
                            continue
                        for k in range(4):
                            if k in [i, j]:
                                continue
                            for l in range(4):
                                if l in [i, j, k]:
                                    continue

                                for configuration in parenthesis:
                                    try:
                                        combination = f"{configuration[0]}{configuration[1]}{nums[i]} {a} {configuration[2]}{configuration[3]}{nums[j]}{configuration[4]} {b} {configuration[5]}{nums[k]}{configuration[6]}{configuration[7]} {c} {nums[l]}{configuration[8]}{configuration[9]}"

                                        # print(f"{combination} = {eval(combination)}")
                                        if eval(combination) == target:
                                            return f"{combination} = {target}"
                                    except ZeroDivisionError:
                                        pass

    return "no solution"

def ops(abc, target=21):
    operations = ['*', '+', '-', '/']

    for a in operations:
        for b in operations:
            for c in operations:
                result = abc(a, b, c,  target)
                if result:
                    return result

    return "no solution"

def abc(a, b, c, stuff):
    for i in range(4):
        for j in range(4):
            if j == i:
                continue
            for k in range(4):
                if k in [i, j]:
                    continue
                for l in range(4):
                    if l in [i, j, k]:
                        continue

                    result = stuff(a, b, c, i, j, k, l)
                    if result:
                        return result;

import random

for i in range(10):
    nums = []

    for i in range(4):
        nums.append(random.randint(1, 13))

    print(nums)
    print(go21(nums))
    print()
