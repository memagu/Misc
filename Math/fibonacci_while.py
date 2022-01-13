prev_num = 0
curr_num = 1

n = int(input())
count = 0

while count < n:
    count += 1
    temp = prev_num
    prev_num = curr_num
    curr_num = temp + curr_num

if n == 0:
    print(0)
else:
    print(prev_num)