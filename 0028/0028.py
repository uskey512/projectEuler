squareSize = 1001
result     =    1

for i in range(3, squareSize + 1, 2):
    result += 4 * i * i - 6 * (i - 1)

print(result)
