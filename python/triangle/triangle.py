from typing import List

def diff_sides(sides: List[int]) -> int:
    sides = sorted(sides)

    def is_invalid():
        return (
            (sides[0] + sides[1] < sides[2])  # impossible triangle
            or (sum(sides) == 0)  # is it a point ?
        )

    return (
        0
        if is_invalid()
        else len(set(sides))  # qty of differtents sides length
    )

def equilateral(sides: List[int]) -> bool:
    return diff_sides(sides) == 1


def isosceles(sides: List[int]) -> bool:
    return diff_sides(sides) in [1, 2]  # equilateral is isoceles as well


def scalene(sides: List[int]) -> bool:
    return diff_sides(sides) == 3
