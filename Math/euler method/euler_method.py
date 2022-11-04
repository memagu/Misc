# def y_(x, y):
#     return 4 - x * y

def y_(x, y):
    return 9.82 - 0.0025*y**2


n_iterations = 1000
step_size = 0.01

x = 0
y = 0
y_next = y + y_(x, y) * step_size

for i in range(n_iterations):
    print(f"{i=}, {x=:.2f}, {y=:.2f}, {y_(x,y)=:.2f}", end=", ")
    y += y_(x, y) * step_size
    print(f"y_next={y:.2f}")
    x += step_size