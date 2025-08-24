def candy_in_the_box(N, K):
    if N > K:
        return K
    elif 2 * N > K:
        return 2 * N - K
    else:
        if candy_in_the_box(N, (K % (2 * (N - 1)))) == 0:
            return 2
        else:
            return candy_in_the_box(N, (K % (2 * (N - 1))))
T = int(input())
testcase = []
box_index = []
for i in range(T):
    N, K = map(int, input().split(" "))
    box_index.append(candy_in_the_box(N, K))
for i in box_index:
    print(i)

'''T = int(input())
testcase = []
for i in range(T):
    N, K = map(int, input().split())
    testcase.append((N, K))
box_index = []
for N, K in testcase:
    position = 1 + ((K-1) % (2*N-2))
    box_index.append(position)
for i in box_index:
    print(i)'''

'''def candy_in_the_box(testcase):
    box_index = []
    for N, K in testcase:
        if K <= N:
            box_index.append(K)
        elif K > N:
            position = 0
            K = K - N
            while K > 0:
                for i in range(N-2, -1, -1):
                    K -= 1
                    if K == 0:
                        position = i + 1
                        break
                for i in range(1, N):
                    K -= 1
                    if K == 0:
                        position = i + 1
                        break
            box_index.append(position)
    return box_index
T = int(input())
testcase = []
for i in range(T):
    N, K = map(int, input().split(" "))
    testcase.append((N, K))
box_index = candy_in_the_box(testcase)
for i in box_index:
    print(i)'''