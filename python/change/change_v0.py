def find_coins(total_change, coins):
    changes = []

    for k, c in enumerate(coins):
        while total_change >= 0:
            next_change = total_change - c
            diff_than_zero = next_change != 0

            try:
                next_coin = coins[k+1]
            except IndexError:
                next_coin = False

            print(f"puis je prendre une piece de {c} ?")
            if next_coin and next_change % next_coin == 0:
                changes.append(c)
                total_change = next_change
                print(f"Ok, pour le prochain")
                break
            elif next_coin and (total_change % next_coin == 0):
                print("Non, par contre")
                take_lot = (total_change // next_coin)
                changes.extend([next_coin] * take_lot)
                print(f"je prend {take_lot} pieces de {next_coin} ")
                return sorted(changes)
            if next_change < coins[-1]:
                print("Non, piece suivante")
                break
            print(f"je prend une piece de {c}")
            changes.append(c)
            total_change = next_change
    # if total_change == 0:
    #     return sorted(changes)
    # return False


def find_minimum_coins(total_change, coins):
    if total_change == 0:
        return []

    if total_change < 0:
        raise ValueError("Cannot as for negative change")

    coins = sorted([c for c in coins if c <= total_change])

    r = []
    while len(coins):
        found = find_coins(total_change, coins[::-1])
        if found:
            r.append(found)
        coins.pop()
    if r == []:
        raise ValueError("No change possible")
    print(r)
    return sorted(r, key=lambda x: len(x))[0]
    # return find_coins(total_change, coins)


def main():
    print(find_minimum_coins(15, [1, 5, 10, 25, 100]))


if __name__ == '__main__':
    main()
