from math import gcd, sqrt


def primitive_triplets(b):
    if b % 4:
        raise ValueError(f"{b} must be %4")

    # init results
    r = []
    nm = b//2

    for n in range(1, int(sqrt(nm)) + 1):
        for m in range(1, (nm//n) + 1):
            if (b == 2*m*n) and (m > n) and ((m-n) % 2 == 1) and gcd(m, n) == 1:
                a = m**2 - n**2
                c = m**2 + n**2
                r.append(tuple(sorted([a, b, c])))
    return set(r)


def triplets_in_range(start, end):
    r = []
    for c in range(start, end + 1):
        for b in range(start, c):
            for a in range(start, b):
                s = (a, b, c)
                if is_triplet(s):
                    r.append(s)
    return set(r)


def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return a**2 + b**2 == c**2


def main():
    print(primitive_triplets(84))


if __name__ == '__main__':
    main()
