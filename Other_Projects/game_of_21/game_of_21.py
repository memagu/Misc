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

    # 0 | 1 + 1 + 1 + 1
    # 1 | 1 + (1 + 1) + 1
    # 2 | (1 + (1 + 1)) + 1
    # 3 | 1 + ((1 + 1) + 1)
    # 4 | (1 + 1) + 1 + 1
    # 5 | ((1 + 1) + 1) + 1
    # 6 | 1 + 1 + (1 + 1)
    # 7 | 1 + (1 + (1 + 1))
    # 8 | (1 + 1) + (1 + 1)

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


import random

for i in range(10):
    nums = []

    for i in range(4):
        nums.append(random.randint(1, 13))

    print(nums)
    print(go21(nums))
    print()
