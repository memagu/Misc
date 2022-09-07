N, M = map(int, input().split())
[print(i) for i in range(min(M, N) + 1, max(M, N) + 2)]

N = 7
M = 6

for i in range(1, M+1):
    print([j+i for j in range(1, N+1)])