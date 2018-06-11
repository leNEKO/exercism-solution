# :( i really need to learn some math

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)

DIR = [NORTH, EAST, SOUTH, WEST]  # his uglyness


class Robot(object):
    ''' well… it works '''

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    def turn_right(self):
        k = DIR.index(self.bearing)
        n = (k+1) % len(DIR)
        self.bearing = DIR[n]

    def turn_left(self):
        k = DIR.index(self.bearing)
        n = (k-1) % len(DIR)
        self.bearing = DIR[n]

    def advance(self):
        x, y = self.bearing
        self.x += x
        self.y += y

    def simulate(self, inst: str):
        # shame loop
        for c in inst:
            if c == "R":
                self.turn_right()
            if c == "L":
                self.turn_left()
            if c == "A":
                self.advance()

    @property
    def coordinates(self):
        return (self.x, self.y)
