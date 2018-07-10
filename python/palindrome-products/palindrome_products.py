def largest_palindrome(min_factor, max_factor):
    return prod_palindrome(max_factor, min_factor, step=-1)


def smallest_palindrome(min_factor, max_factor):
    return prod_palindrome(min_factor, max_factor, step=1)


def prod_palindrome(min_factor, max_factor, step=1):
    hiscore = max_factor**2 if step > 0 else 0
    factors = None

    for i in range(min_factor, max_factor + step, step):
        for j in range(min_factor, max_factor + step, step):
            p = i * j
            higher = p > hiscore
            lower = p < hiscore
            if higher if step > 0 else lower:
                break  # no need to check more
            if(str(p) == str(p)[:: -1]):
                if lower if step > 0 else higher:
                    hiscore = p
                    factors = [tuple(sorted([i, j]))]
                elif(p == hiscore):
                    factors.append(tuple(sorted([i, j])))

    if not factors:
        raise ValueError("Nothing")

    return hiscore, factors
