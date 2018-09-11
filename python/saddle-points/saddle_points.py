def saddle_points(matrix):
    if matrix == []:  # return empty set if empty matrix
        return set()

    # test for irregular matrix
    if len(set(len(r) for r in matrix)) > 1:
        raise ValueError("Irregular matrix")

    # init list
    rows = matrix
    columns = [*zip(*matrix)]  # wow what a shortcut :)

    sp = set()
    for y, row in enumerate(rows):
        max_in_row = max(row)  # max value in row
        for x, val in enumerate(row):
            min_in_col = min(columns[x])  # min value in column
            if (val == min_in_col) and (val == max_in_row):
                sp.add((y, x))
    return sp
