def grid_traveler(x, y, memo={}):
    if (x, y) in memo:
        return memo[(x, y)]
    if x == 1 and y == 1:
        return 1
    if x == 0 or y == 0:
        return 0

    memo[(x, y)] = grid_traveler(x-1, y, memo) + grid_traveler(x, y-1, memo)
    return memo[(x, y)]


print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(500, 500))