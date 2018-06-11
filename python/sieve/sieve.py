def sieve(limit):
    nums = list(range(limit+1))
    nums[1] = 0
    for i in nums:
        if i:
            for y in range(2*i, limit+1, i):
                nums[y] = 0
    return [i for i in nums if i > 0]
