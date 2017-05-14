from decimal import *

def getLongestCommonSubstring(check):
    maxLength     = 0
    maxLengthWord = ''

    for start in range(len(check)):
        for end in range((start+1),len(check)):
            subword = check[start:end]
            if 1 < check.count(subword):
                maxLengthWord = subword
                maxLength     = check.count(subword)

    #message = '{0}, counts {1}'.format(maxLength, maxLengthWord)
    #print(message)

    return maxLength

DIGITS = 110
getcontext().prec = DIGITS

for i in range(1, 1000):
    asString  = str(Decimal(1) / Decimal(i))[0:(DIGITS - 10)]
    maxLength = getLongestCommonSubstring(asString)

    result = '{0:4d}, {2:3d} : {1}'.format(i, Decimal(1) / Decimal(i), maxLength)
    print(result)
