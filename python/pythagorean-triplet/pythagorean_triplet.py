def is_even(a):
    return False if a % 2 else True


def is_coprime(m, n):
    if m <= n:
        raise ValueError('Error: m <= n')

    if is_even(m) and is_even(n):
        return False

    for divisor in range(3, n+1):
        if (m % divisor == 0) and (n % divisor == 0):
            return False

    return True


def is_odd_difference(m, n):
    if m <= n:
        raise ValueError('Error: m <= n')

    return True if (m - n) % 2 else False


def primitive_triplets(b):
    if b % 4:
        raise ValueError('Error: b is not devidable to 4')

    # mn = int(b / 2)
    mn_list = []

    for n in range(1, b+1):
        for m in range(n+1, b+1):
            if (b == 2 * m * n) and is_odd_difference(m, n) and is_coprime(m, n):
                mn_list.append((m, n))

    result = []

    for m, n in mn_list:
        a = m ** 2 - n ** 2
        c = m ** 2 + n ** 2
        if not (is_even(a) and is_even(c)):
            triplet = [a, b, c]
            return(triplet)
            triplet.sort()
            result.append(tuple(triplet))

    return set(result)


def triplets_in_range(min, max):
    result = []
    for a in range(min, max+1):
        for b in range(min, max+1):
            for c in range(min, max+1):
                if c > a and c > b and a < b and is_triplet((a, b, c)):
                    result.append((a, b, c))

    return set(result)


def is_triplet(args):
    args_list = list(args)
    args_list.sort()
    sorted_args = tuple(args_list)
    a, b, c = sorted_args
    return a ** 2 + b ** 2 == c ** 2


def main():
    print(primitive_triplets(26**2*10**3))


if __name__ == '__main__':
    main()
