def binary_search(l, n):
    ll = len(l)  # list length
    h = ll // 2  # half length
    o = h  # offset

    if l == []:
        raise ValueError("Empty array")

    if (l[0] <= n <= l[-1]) == False:
        raise ValueError("Out of bound")

    while True:
        print(f"search {n} at {o} found {l[o]}")
        if l[o] == n:
            print("WIN!")
            return o
        h //= 2
        o += h if l[o] <= n else -h
        print(f"next offset {o}")
        if h == 0:
            raise ValueError("Not Found")


def main():
    print(
        binary_search([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21)
    )


if __name__ == '__main__':
    main()
