from melvec import *
import math

v1 = Vec3(1, 0)
v2 = Vec3(3, 2)
print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1 / 2)
if v1:
    print("True")
print()
print(Vec2())
print(v2.normalize())
Vec3().from_angle()

print(Vec2.from_angle(math.pi/6, 1))

v21 = Vec2(0, 1)
v22 = Vec2(3, 4)

print(Vec2.from_angle(v21.angle_to(v22), 5))

