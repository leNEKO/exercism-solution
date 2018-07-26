def square_of_sum(count: int) -> int:
    return sum(i for i in range(count+1)) ** 2


def sum_of_squares(count: int) -> int:
    return sum(i**2 for i in range(count+1))


def difference(count: int) -> int:
    return square_of_sum(count) - sum_of_squares(count)
