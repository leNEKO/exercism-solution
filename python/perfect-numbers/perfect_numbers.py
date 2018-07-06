'''
allright here the square math trick (that i don't understand …)
'''


def classify(number):
    if number <= 0:
        raise ValueError("don't 0 m8")
    if number == 1:
        return "deficient"

    # it seems that if first bit == 1 of tha
    aliquot_sum = 1
    # greatest divisor cannot be greater than half the value
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            aliquot_sum += i
            if not i == number//i:
                aliquot_sum += number//i
            if aliquot_sum > number:
                return "abundant"  # substantial optimization :|

    if aliquot_sum == number:
        return "perfect"

    return "deficient"
