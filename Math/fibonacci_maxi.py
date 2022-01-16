# Maxis val av variabler

fibbe = [0, 1]
for fibbes_mamma in range(1, int(input())):
    fibbe.append(fibbe[fibbes_mamma] + fibbe[fibbes_mamma-1])
    print(fibbe[-1])

# 0, 1, 1, 2, 3, 5

