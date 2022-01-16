prev_num = 0
curr_num = 1

n = int(input())

for i in range(n):
    temp = prev_num
    prev_num = curr_num
    curr_num = temp + curr_num

if n == 0:
    print(0)
else:
    print(prev_num)
