

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
                            if k == j or k == i:
                                continue
                            for l in range(4):
                                if l == k or l == j or l == i:
                                    continue



                                combination = f"{nums[i]} {a} {nums[j]} {b} {nums[k]} {c} {nums[l]}"

                                print(f"{combination} = {eval(combination)}")

                                if eval(combination) == 21:
                                    pass
                                    # return f"{combination} = 21"

    return "no solution"


import random

random.seed(3)
nums = []

for i in range(4):
    nums.append(random.randint(1, 13))

print(nums)
print(go21(nums))