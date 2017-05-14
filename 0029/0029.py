from numpy import *

SIZE = 5
MAX  = SIZE
matrix = [[True for i in range(SIZE + 1)] for j in range(SIZE + 1)]

def getPrimeFactors(x):
    result = []

    while x != 1:
        for i in range(2, SIZE):
            if x % i == 0:
                result.append(i)
                x /= i
                break

    return result

def getPairedFactor(primeFactors):
    for i in range(len(primeFactors)):
        prod = 1
        for j in range(len(primeFactors)):
            if i != j:
                prod *= primeFactors[j]
        yield [primeFactors[i], prod]

for i in range(2, SIZE + 1):
    for j in range(2, SIZE + 1):
        if matrix[i][j] == True:
            factors = getPrimeFactors(j)
            if len(factors) < 2:
                continue
            gen = getPairedFactor(factors)
            for pairedFactors in range(len(factors)):
                pair = gen.next()
                base = i**pair[0]
                if base <= SIZE and pair[1] <= SIZE:
                    matrix[base][pair[1]] = False

cnt = 0
for i in range(2, SIZE + 1):
    for j in range(2, SIZE + 1):
        if matrix[i][j] == True:
            cnt += 1


# 指数を素因数分解して、素因数の数が2以上になれば
# 以降の値と同じ値となるはず ex.) 3 ^ 6 = 3 ^ (2 * 3) = 9 ^ 3
# [底][指数] の [100][100]boolean(:True)配列用意して
# 2から順に見ていってTrueであれば、以降の値での別表現が無いかを
# 指数素因数分解して、底が100以下のパターンならFalseを突っ込む
# で、動くはずだけど動かないので一旦現状コードを保存

print(cnt)
