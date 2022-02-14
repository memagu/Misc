with open("out.txt", "w") as f:
    def go21(nums):
        operations = ['*', '+', '-', '/']

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

                                    combination = f"{nums[i]} {a} {nums[j]} {b} {nums[k]} {c} {nums[l]}"
                                    # f.write(f"{combination} = {eval(combination)}\n")

                                    # print(f"{combination} = {eval(combination)}")

                                    if eval(combination) == 21:
                                        return f"{combination} = 21"

        return "no solution"


    import random

    nums = []

    for i in range(4):
        nums.append(random.randint(1, 13))

    print(nums)
    print(go21(nums))