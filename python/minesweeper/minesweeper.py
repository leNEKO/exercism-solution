NEIGHBORHOOD = [(ox, oy) for ox in [-1, 0, 1]
                for oy in [-1, 0, 1] if (ox, oy) != (0, 0)]  # all around but itself


def board(input_board_array):
    # well i prefer go OOP
    g = Game(input_board_array)
    return g.solved


class Game:
    def __init__(self, board):
        self.board = dict()

        # check for Irregular board
        if len(set(len(r) for r in board)) > 1:
            raise ValueError("Irregular board")

        # fill the board
        for coord, val in (((x, y), val) for y, line in enumerate(board) for x, val in enumerate(line)):
            self.board[coord] = Point(self, coord, val)

        # solve the board
        tab = [""] * len(board)
        for coord, point in self.board.items():
            x, y = coord
            tab[y] += point.count_mines()

        self.solved = tab


class Point:
    def __init__(self, parent, coord, val):
        if val not in " *":
            raise ValueError("Irregular point")

        self.parent = parent
        self.coord = coord
        self.val = val

    def count_mines(self):
        board = self.parent.board
        x, y = self.coord

        # if is a mine
        if(self.val == "*"):
            return "*"

        mines = 0
        for ox, oy in NEIGHBORHOOD:
            ncoord = (x + ox, y + oy)
            if ncoord in board:
                mines += board[ncoord].val == "*"

        return str(mines or " ")
