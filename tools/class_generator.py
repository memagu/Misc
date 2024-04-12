def generate_class(name: str, *args: str):
    print(f"class {name}:")
    print("    " + f"def __init__(self, {', '.join(args)}):")
    for arg in args:
        print("        " + f"self.{arg} = {arg}")


generate_class("TestClass", "name", "size", "color", "tag", "id", "pos", "velocity", "acceleration", "direction")
generate_class("PendulumArm", "length", "mass", "angle", "angle_velocity", "angle_acceleration")
