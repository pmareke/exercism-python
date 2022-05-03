def factors(value):
    divisors = []
    i = 2

    while pow(i, 2) <= value:
        while value % i == 0:
            value /= i
            divisors.append(i)
        i += 1
    if value > 1:
        divisors.append(value)
    return divisors
