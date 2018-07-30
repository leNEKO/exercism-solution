def append(xs, ys):
    return xs + ys


def concat(lists):
    return [item for sublist in lists for item in sublist]


def filter_clone(function, xs):
    return [item for item in xs if function(item)]


def length(xs):
    # :|
    return sum([1 for _ in xs])


def map_clone(function, xs):
    return [function(item) for item in xs]


def foldl(function, xs, acc):
    r = acc
    for item in xs:
        try:
            r = function(item, r)
        except ZeroDivisionError:
            return 0
    return r


def foldr(function, xs, acc):
    r = acc
    for item in xs[::-1]:
        try:
            r = function(item, r)
        except ZeroDivisionError:
            return 0
    return r


def reverse(xs):
    return xs[::-1]
