''' is there some math mojo i don't know to do this without a loop ? '''


def square_of_sum(count: int) -> int:
    sum: int = 0
    for i in range(1, count+1):
        sum += i
    return sum**2


def sum_of_squares(count: int) -> int:
    sum: int = 0
    for i in range(1, count+1):
        sum += i**2
    return sum


def difference(count: int) -> int:
    return square_of_sum(count) - sum_of_squares(count)
