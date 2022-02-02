def can_sum(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in arr:
        if target >= num:
            if can_sum(target - num, [e for e in arr if e != num]):
                memo[target] = True
                return memo[target]

    return False


print(can_sum(9, [5, 3, 4, 7]))
