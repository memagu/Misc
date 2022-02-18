def radio_tower(numbers, multipliers, target):
    for i in range(3):
        for j in range(3):
            if j == i:
                continue
            for k in range(3):
                if k in [j, i]:
                    continue

                for l in range(3):
                    for m in range(3):
                        if m == l:
                            continue
                        for n in range(3):
                            if n in [m, l]:
                                continue

                            combination = f"{numbers[i]} * {multipliers[l]} + {numbers[j]} * {multipliers[m]} + {numbers[k]} * {multipliers[n]}"
                            if eval(combination) == target:
                                return f"{numbers[i]} * {multipliers[l]}\t\\\n{numbers[j]} * {multipliers[m]}\t --  {target}\n{numbers[k]} * {multipliers[n]}\t/"
    return "No solution."


while True:
    nums = [int(num) for num in input("Enter the numbers: ") if num in [str(i) for i in range(10)]]
    temp = [int(num) for num in input("Enter the multipliers: ") if num in [str(i) for i in range(10)]]
    muls = []
    for num in temp:
        if num != 0:
            muls.append(num)
            continue
        muls.pop(-1)
        muls.append(10)

    # nums = list(map(int, input("Enter the numbers: ").split()))
    # muls = list(map(int, input("Enter the multipliers: ").split()))

    target = int(input("Enter target number: "))

    print(f"\nnumbers = {' '.join([str(e) for e in nums])}\nmultipliers = {' '.join([str(e) for e in muls])}\n")
    print(f"{radio_tower(nums, muls, target)}")
    print(f"\n{'-'*32}\n")

