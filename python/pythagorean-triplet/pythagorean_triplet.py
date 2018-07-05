import numpy as np


def gen_prim_pyth_trips(limit=None):
    # Berggren / Robert / Hall
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield m
        m = np.dot(m, uad)


def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim


def primitive_triplets(n):
    r = []
    for a in gen_prim_pyth_trips(n*2):
        for l in a:
            if n in l:
                r.append(l)
    print(r)


def triplets_in_range(range_start, range_end):
    pass


def is_triplet(triplet):
    pass


def main():
    primitive_triplets(84)


if __name__ == '__main__':
    main()
