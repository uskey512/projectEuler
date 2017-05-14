squareSize = 1001
result     =    0

for lengthOfOneSide in range(1, squareSize + 1, 2):
    if lengthOfOneSide == 1:
        result += 1
    else:
        result += 4 * lengthOfOneSide * lengthOfOneSide - 6 * (lengthOfOneSide - 1)

print(result)
