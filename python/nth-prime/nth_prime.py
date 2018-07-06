from math import log


def nth_prime(n):
    # approximative sieve length (i don't remember how it works)
    limit = max(20, int(n * log(n) * 1.3))
    sieve = [i for i in range(0, limit + 1)]

    k = 0
    for e in range(0, limit+1):
        if sieve[e] > 1:
            k += 1
            i = e ** 2
            if(k == n):
                return e
            while i <= limit:
                sieve[i] = 0
                i += e
