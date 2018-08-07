from itertools import combinations


def find_minimum_coins(total_change: int, coins: list) -> list:
    if total_change == 0:
        return []  # an empty list if no change

    # Validate input
    if total_change < 0:
        raise ValueError("No negative change")

    # init best combination
    best = False

    # I will use "compound" coins instead of the "atomical" coins
    c_coins = compound_coins(coins)
    # filter out virtual coins with values greater than total_change
    c_coins = list(filter(lambda x: sum(x) <= total_change, c_coins))

    # will remove one compound coin from the coins configuration per iteration
    for i in range(len(c_coins)):
        # init a combination
        change = []
        total = total_change
        for c_coin in c_coins[::-1][i:]:
            c_coin_val = sum(c_coin)
            while (total - c_coin_val) >= 0:
                # add the compound coin tuple to the combination list
                change += list(c_coin)
                total -= c_coin_val

        # jump to next iteration if no result were found within the current coins configuration
        if total != 0:
            continue

        # replace the best combination only if a better one were found
        if best is False or (len(change) < len(best)):
            best = change

    if best is False:
        raise ValueError("No combinations exists")

    # we need to optimize this a little more :
    return optimize_coins(coins, best)


def compound_coins(coins: list) -> list:
    '''
    Return a list of tuples of all coins combinations, ex.:
    for a list of 4,5 coins we will have an extra compound coin of value 9
    [(4,), (5,), (4,5)] -> [4,5,9]

    Arguments:
        coins {list} -- a list of coins ex.: [4,5]

    Returns:
        list -- a list of tuples ex.: [(4,), (5,), (4,5)]
    '''
    return sorted(
        [comb for l in range(1, len(coins)+1)
         for comb in combinations(coins, l)],
        key=lambda x: sum(x)
    )


def optimize_coins(coins: list, comb: list) -> list:
    '''
    Perform some cleaning because of compound coins design :|

    Arguments:
        coins {list} -- coins list
        comb {list} -- change combination that would need optimizatrion

    Returns:
        list -- optimized and sorted list of coins
    '''

    # failed to observe the "flat is better than nested" rule :(
    coins = coins[::-1]  # bigger to lower
    for idx in range(len(coins)):
        coin = coins[idx]
        for next_coin in coins[idx+1:]:
            div, res = divmod(coin, next_coin)
            if res == 0:  # if the coin can be made of a next_coin
                count = comb.count(next_coin)
                sub_div, res = divmod(count, div)
                if sub_div:
                    # remove all coin of next_coin value
                    comb = list(filter(lambda a: a != next_coin, comb))
                    # replace them by sub_div * coin
                    comb += [coin] * sub_div
                    # + the next_coin * res
                    comb += [next_coin] * res
                    break  # no need to go further
    return sorted(comb)
