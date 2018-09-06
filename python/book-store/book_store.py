# groups prices
PRICES = {
    1: 800,  # no discount
    2: 1520,  # 5 %
    3: 2160,  # 10 %
    4: 2560,  # 20 %
    5: 3000  # 25 %
}


def calculate_total(books):
    best = float("inf")  # highest price possible
    i = 0

    # let's try each combinations
    for mx in list(PRICES.keys())[1:]:
        groups = []  # init groups
        bks = books[::-1]  # make a reversed copy of books

        while bks:
            book = bks.pop()  # pop 1 book
            found_group = False  # …

            # append the book in an existing group if possible
            for k, vals in enumerate(groups):
                i += 1
                if book not in vals and len(vals) < mx:
                    groups[k].append(book)
                    found_group = True  # …
                    break  # jump to next iteration

            # if book is already in every existing groups
            if found_group is False:
                groups.append([book])  # create a new group

        # calculate total of this current group combination
        total = sum([PRICES[len(group)] for group in groups])
        # record it as best result if lower price
        best = total if total < best else best

    return best
