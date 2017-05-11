def get_fibonachi_even_sum(maxOfNumber):
    a      = 1
    b      = 2
    result = 0
    tmp    = 0

    while b <= maxOfNumber:
        if b % 2 == 0:
            result += b
        tmp = a + b
        a   = b
        b   = tmp

    return result

print(get_fibonachi_even_sum(4000000))
