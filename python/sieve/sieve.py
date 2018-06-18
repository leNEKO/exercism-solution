def sieve(limit):
    nums = list(range(limit+1))
    nums[1] = 0
    for i in nums:
        if i:
            for y in range(i**2, limit+1, i):
                nums[y] = 0
    return [i for i in nums if i > 0]


def gen_primes(limit):
    """ Generate an infinite sequence of prime numbers."""
    marked_not_prime = {}
    value_to_check = 2
    while True and value_to_check < limit:
        if value_to_check not in marked_not_prime:
            yield value_to_check
            marked_not_prime[value_to_check *
                             value_to_check] = [value_to_check]
        else:
            for prime in marked_not_prime[value_to_check]:
                marked_not_prime.setdefault(
                    prime + value_to_check, []).append(prime)
            del marked_not_prime[value_to_check]
        value_to_check += 1


print(sieve(100), list(gen_primes(100)))
