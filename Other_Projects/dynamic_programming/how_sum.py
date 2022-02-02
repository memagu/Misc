def how_sum(target, arr, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for num in arr:
        result = how_sum(target - num, arr)

        if result != None:
            memo[target] = [*result, num]
            return memo[target]

    return None


print(how_sum(9, [5, 3, 4, 7]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(5, [5, 3, 4, 7]))
print(how_sum(16, [5, 3, 4, 7]))
print(how_sum(20, [5, 3, 4, 7]))
