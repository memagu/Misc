def clamp(val, minv, maxv):
    return max(min(val, maxv), minv)

def inv_lerp(a, b, val) -> float:
    temp = (val - a) / (b - a)
    return clamp(temp, 0, 1)

print(inv_lerp(0, 10, -1))
