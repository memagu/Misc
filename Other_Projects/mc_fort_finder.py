import math


def mc_deg_to_rad(mc_degrees: float) -> float:
    if mc_degrees < 0:
        mc_degrees = 360 + mc_degrees

    return math.radians(mc_degrees + 90)


data1 = tuple(
    map(float, input("Enter x, z and direction (in degrees) values of first point separated by space: ").split()))
data2 = tuple(
    map(float, input("Enter x, z and direction (in degrees) values of second point separated by space: ").split()))

p1, p2 = data1[:2], data2[:2]
k1, k2 = math.tan(mc_deg_to_rad(data1[-1])), math.tan(mc_deg_to_rad(data2[-1]))
m1, m2 = p1[1] - k1 * p1[0], p2[1] - k2 * p2[0]

fort_x = (m2 - m1) / (k1 - k2)
fort_z = k1 * fort_x + m1

print(f"\nCoordinates of fort calculated to be: (x={fort_x:.3f}, z={fort_z:.3f}). Keep in mind that inaccuracies in the inputed direction values may cause inaccurate results.")

input("\nDone! Press enter to exit.")
