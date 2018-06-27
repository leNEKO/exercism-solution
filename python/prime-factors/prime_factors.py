# literral translation of my javascript solution
def prime_factors(natural_number):
    primes = []
    i = 2
    while natural_number >= i:
        while (natural_number % i) == 0:
            primes.append(i)
            natural_number /= i
        i += 1

    return primes
