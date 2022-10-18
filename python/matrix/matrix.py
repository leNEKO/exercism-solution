from typing import List

class Matrix(object):
    def __init__(self, input: str):
        self.rows: List[List[int]] = [
            [int(i) for i in input_row.split(' ')]
            for input_row in input.split('\n')
        ]
        self.columns: List[List[int]] = [
            list(column)
            for column in zip(*self.rows)
        ]

    def row(self, index: int) -> List[int]:
        return self.rows[index-1]

    def column(self, index: int) -> List[int]:
        return self.columns[index-1]
