def binary_search(num_list, num):
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

        # stretch the slice
        if num_list[middle] < num:
            start = middle  # new slice start
        else:
            end = middle  # new slice end
