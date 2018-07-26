def diff_sides(sides):
    sides = sorted(sides)
    if (
        (sides[0] + sides[1] < sides[2])  # impossible triangle
        or (sum(sides) == 0)  # is it a point ?
    ):
        return 0
    return len(set(sides))  # qty of differents sides lengths


def is_equilateral(sides):
    return diff_sides(sides) == 1


def is_isosceles(sides):
    return diff_sides(sides) in [1, 2]  # equilateral is isoceles as well


def is_scalene(sides):
    return diff_sides(sides) == 3
