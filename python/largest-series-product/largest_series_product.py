
'''
near plain translation of my php solution, nothing very pythonic
'''
from functools import reduce
import re


def largest_product(series: str, size: int) -> int:
    if series != re.sub(r"/\D/", "", series):
        raise ValueError("Invalid input")

    ser_size = len(series)
    if size > ser_size:
        raise ValueError("Size > series length")

    if not ser_size or not size:
        return 1

    if size < 0:
        raise ValueError("Size must be >= 0")

    hi_product = 0
    for i in range(0, ser_size - size + 1):
        ser_slice = series[i:i+size]
        product = reduce(lambda a, b: int(a)*int(b), ser_slice)
        if product > hi_product:
            hi_product = product

    return hi_product
