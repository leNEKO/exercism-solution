def append(xs, ys):
    return concat([xs, ys])


def concat(lists):
    return [item for sublist in lists for item in sublist]


def filter_clone(function, xs):
    return [item for item in xs if function(item)]


def length(xs):
    return sum(1 for _ in xs)


def map_clone(function, xs):
    return [function(item) for item in xs]


def foldl(function, xs, acc):
    for item in xs:
        acc = function(acc, item)
    return acc


def foldr(function, xs, acc):
    for item in reverse(xs):
        acc = function(item, acc)
    return acc


def reverse(xs):
    return xs[::-1]
