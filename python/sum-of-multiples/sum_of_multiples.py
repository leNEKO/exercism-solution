def sum_of_multiples(limit, multiples):
    nums = set(i for i in range(1, limit) for k in multiples if i % k == 0)
    return sum(nums)
