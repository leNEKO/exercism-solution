'''
BEWARE : it is an incomplete solution,
and i think it cannot be completed without rewriting all :(
'''

PRICE = 800  # price in cents
DISCOUNTS = {
    2: 5,
    3: 10,
    4: 20,
    5: 25
}


def calculate_by_copies(copies, total=0, max=5):
    # while the books list not empty
    if sum(copies):
        # counting
        diff_books = 0
        for k, qty in enumerate(copies):
            if copies[k] != 0:
                copies[k] -= 1  # remove a book from the list
                diff_books += 1  # count it as a diff book

        # get discount
        try:
            discount = DISCOUNTS[diff_books]
        except KeyError:
            discount = 0

        price = int(PRICE * (1 - discount * 0.01))

        # update total price
        total += diff_books * price

        # recursion
        return calculate_by_copies(copies, total)

    return total


def calculate_total(books):
    # make a list of copies count from the books idx list
    copies = list({x: books.count(x) for x in books}.values())
    return calculate_by_copies(copies) or 0


def main():
    print(
        calculate_total([1, 1, 2, 2, 3, 3, 4, 5])
    )


if __name__ == '__main__':
    main()
