def factorial(N):
    if N == 0:
        return 1
    else:
        factorial_of_the_number = N * factorial(N-1)
    return factorial_of_the_number
N = int(input())
factorial_of_the_number = factorial(N)
print(factorial_of_the_number)