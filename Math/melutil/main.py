from melvec2 import *
from melcoordsys import *
from melmatrix import *
import math

c1 = Coordsys2d(Vec2(1, 1), Vec2(-1, 1), Vec2(1, 1))

print(c1.local_to_world(Vec2(1, 1)))
print(c1.world_to_local(c1.local_to_world(Vec2(1, 1))))

c2 = Coordsys3d(Vec3(1, 1, 0), Vec3(-1, 1, 0), Vec3(0, 0, 0), Vec3(1, 1, 0))

print(c2.local_to_world(Vec3(1, 1, 0)))
print(c2.world_to_local(c2.local_to_world(Vec3(1, 1, 0))))

