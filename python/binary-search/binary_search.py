'''
A recursive attempt but it only consist of getting rid of the 'while' loop
i don't see much benefit over the main iterative function (and it is around twice slower)
'''


def binary_search(num_list, num, start=0, end=None):
    # num_list can't be empty
    if num_list == []:
        raise ValueError("Empty array")

    # init end
    if end is None:
        end = len(num_list)

    half = (end - start) // 2
    middle = start + half  # middle of the slice

    if num_list[middle] == num:
        return middle  # yay found it
    elif start == middle:
        raise ValueError(f"{num} Not in list")  # value not in list

    # shrink
    if num_list[middle] < num:
        start = middle  # new slice start
    else:
        end = middle  # new slice end

    return binary_search(num_list, num, start, end)


'''
So i tried to overwrite the num list with a "hard" sliced version of it and use 'start' to
keep record of the 'offset'. The process of slicing a list seems to take more cpu
than just pass the full num_list to the recursive function
'''


def binary_search_recursive_hard_slice(num_list, num, start=0):
    # num_list can't be empty
    if num_list == []:
        raise ValueError("Empty array")

    middle = len(num_list) // 2
    center_num = num_list[middle]  # num in the middle

    if center_num == num:
        # yay ! (don't forget to add the start offset as the num_list changed length)
        return start + middle
    elif middle == 0:
        raise ValueError(f"{num} Not in list")

    # slice the num_list then recurse
    if center_num < num:
        return binary_search(num_list[middle:], num, start + middle)
    else:
        return binary_search(num_list[:middle], num, start)


''' the original iteration that so far is the fatest '''


def binary_search_iterative(num_list, num):
    # num_list can't be empty
    if num_list == []:
        raise ValueError("Empty array")

    # init slice
    start = 0
    end = len(num_list)

    while True:
        half = (end - start) // 2
        middle = start + half  # middle of the slice

        if num_list[middle] == num:
            return middle  # yay found it
        elif start == middle:
            raise ValueError(f"{num} Not in list")  # value not in list

        # shrink
        if num_list[middle] < num:
            start = middle  # new slice start
        else:
            end = middle  # new slice end


def binary_search_dandek(list_of_numbers, number, lo=0, hi=None):
    if hi is None:
        hi = len(list_of_numbers)

    pos = (hi + lo) // 2

    if lo >= hi:
        raise ValueError(f'{number} not in  list')
    if list_of_numbers[pos] == number:
        return pos
    if list_of_numbers[pos] < number:
        return binary_search(list_of_numbers, number, pos + 1, hi)
    return binary_search(list_of_numbers, number, lo, pos)


def binary_search_dandek_iterative(list_of_numbers, number):
    lo, hi = 0, len(list_of_numbers) - 1
    while lo <= hi:
        pos = (lo + hi) // 2
        if number == list_of_numbers[pos]:
            return pos
        if number < list_of_numbers[pos]:
            hi = pos - 1
        else:
            lo = pos + 1
    raise ValueError("Not in list")


from math import floor, ceil, log, inf


def step_size2(length):
    step_size = 1
    # large steps forward
    while step_size < length:
        step_size *= 16
    # small steps backward
    while step_size > length:
        step_size //= 2
    return step_size


def binary_search_ptillemans(list_of_numbers, number):

    length = len(list_of_numbers)
    # find largest power of 2 <= lenght
    step = step_size2(length)

    # offset for 0-based indexing
    mid = step - 1

    while step > 0:
        # half search space
        step = step // 2

        # over upper bound treat as too high
        if mid >= length:
            val = inf
        else:
            val = list_of_numbers[mid]

        if val == number:
            return mid
        elif val < number:
            mid = mid + step
        else:
            mid = mid - step

    raise ValueError("no such number in list")


def main():
    from timeit import timeit
    for f in ["binary_search", "binary_search_recursive_hard_slice", "binary_search_iterative", "binary_search_dandek", "binary_search_dandek_iterative", "binary_search_ptillemans"]:
        setup = f"from __main__ import {f}"
        t = [1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 450, 451, 455]
        r = 21
        cmd = f"{f}({t}, {r})"
        print(f, timeit(cmd, setup, number=100000))


if __name__ == '__main__':
    main()
