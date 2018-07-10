
class Queen(object):
    def __init__(self, x, y):
        # validate coord in the 8x8 grid
        if not(0 <= x <= 7) or not (0 <= y <= 7):
            raise ValueError("not in the board")
        self.coord = (x, y)

    def can_attack(self, another):
        x, y = self.coord
        ax, ay = another.coord

        # same position
        if self.coord == another.coord:
            raise ValueError("Queen on queen")

        # horizontal, vertical attack
        if (ax == x) or (ay == y):
            return True

        # diagonal attack
        dx = abs(ax - x)
        dy = abs(ay - y)
        if dx == dy:
            return True

        return False
