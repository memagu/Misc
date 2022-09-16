def y_(x, y):
    return 4 - x * y


n_iterations = 25
step_size = 0.25

x = 0
y = 1
y_next = y + y_(x, y) * step_size

for i in range(n_iterations):
    print(f"{i=}, {x=:.2f}, {y=:.2f}, {y_(x,y)=:.2f}", end=", ")
    y += y_(x, y) * step_size
    print(f"y_next={y:.2f}")
    x += step_size