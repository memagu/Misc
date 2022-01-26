import sys

max_num = sys.maxsize

n = 1_000_000_000
result = set()

with open("prime_to_billion.txt", "w") as f:

    for i in range(2, n + 1):
        if i < max_num and i not in result:
            f.write(str(i) + "\n")
        max_num = i
        result.add(i)

        for j in range(i+i, n+1, i):
            if j < max_num and j not in result:
                f.write(str(j) + "\n")
            max_num = j
            result.add(j)