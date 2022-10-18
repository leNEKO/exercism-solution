def is_armstrong(number):
    as_str = str(number)
    num_len = len(as_str)
    digit_pow_len = [int(x)**num_len for x in as_str]

    return number == sum(digit_pow_len)


def main():
    i = 0

    while True:
        if is_armstrong(i):
            print(i)
        i += 1


if __name__ == '__main__':
    main()
