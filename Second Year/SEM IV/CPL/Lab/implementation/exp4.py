def sumXY(N, sum):
    sum = []
    for integer in N:
        sorted_digits = sorted(integer)
        X_digits = sorted_digits[::2]
        Y_digits = sorted_digits[1::2]
        X = int("".join(X_digits))
        Y = int("".join(Y_digits))
        sum.append(X + Y)
    return sum
T = int(input())
N = []
for _ in range(T):
    N.append(input())
sum = sumXY(N, sum)
for _ in sum:
    print(_)