# Without duck typing
def flatten(iterable):
    r = []
    # passes the tests but will work only with this list of iterable types
    if type(iterable) in [list, tuple, set]:
        for i in iterable:
            r += flatten(i)
    elif iterable is not None:
        r.append(iterable)
    return r
