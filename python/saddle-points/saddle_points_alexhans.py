import operator
import sys
import itertools


def saddle_points(matrix):
    '''
        If the matrix is not irregular
        Determine the extremes (max) of rows
        Determine the extremes (min) of columns (transposed rows)
        intersect the points that appear in both sets
    '''
    if is_irregular_matrix(matrix):
        raise ValueError("The matrix is irregular")

    matrices = ((matrix, max), (transpose_matrix(matrix), min))

    extremes = (get_row_extremes(*x) for x in matrices)

    return set.intersection(*map(flatten_points, extremes))


def flatten_points(extremes):
    ''' Make a flat list out of the "points" lists '''
    return set(itertools.chain.from_iterable([x["points"] for x in extremes]))


def transpose_matrix(matrix):
    return [*zip(*matrix)]


def is_irregular_matrix(matrix):
    # if the matrix is empty, it won't try to access index 0
    return not all(map(lambda x: len(x) == len(matrix[0]), matrix))


def get_func_points(func, i, a):
    extreme_val = func([x["value"] for x in a])
    points = [x["point"] for x in a if x["value"] == extreme_val]
    return {"value": extreme_val, "points": points}


def get_row_extremes(matrix, func):
    '''
    Gets the extremes of rows
    The func parameter determines whether it's max or min
    '''
    is_max = func == max
    comparison = operator.ge if is_max else operator.le
    store = [[] for _ in range(len(matrix))]
    for i, x in enumerate(matrix):
        extreme = 0 if is_max else sys.maxsize
        for j, y in enumerate(x):
            if comparison(y, extreme):
                extreme = y
                point = (i, j) if is_max else (j, i)
                store[i].append({"value": y, "point": point})

    return (get_func_points(func, i, x) for i, x in enumerate(store))
