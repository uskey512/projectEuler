from decimal import *

getcontext().prec = 95

for i in range(1, 1000):
    result = '{0:4d} : {1:.100f}'.format(i, Decimal(1) / Decimal(i))
    print(result)
