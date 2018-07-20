def find_minimum_coins(total_change, coins):
    # reverse sort and remove coins that values more than the total change
    coins = sorted(v for v in coins if v <= total_change)[::-1]  # rev

    # init best change configuration
    best = None

    # iterate over each configuration
    for i in range(0, len(coins)):
        change = []
        total = total_change
        conf = coins[i:]
        for val in conf:
            while (total - val) >= 0:
                change.append(val)
                total -= val
                if best is not None and (len(change) >= len(best)):
                    break

        # if no change configuration jump to next configuration
        if (change == []) or (total != 0):
            continue

        print("conf:", conf, "change:", change)
        if (best is None) or (len(change) < len(best)):
            best = change

    return sorted(best)


def main():
    r = find_minimum_coins(27, [4, 5])
    print(r)


if __name__ == '__main__':
    main()
