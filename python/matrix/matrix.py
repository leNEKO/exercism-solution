class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = [[int(i) for i in row_str.split(" ")]
                     for row_str in matrix_string.split("\n")]

        self.columns = [[0 for _ in self.rows]
                        for _ in self.rows[0]]  # init list
        for y, row in enumerate(self.rows):
            for x, val in enumerate(row):
                self.columns[x][y] = val  # x,y <- y,x

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return self.columns[index]
