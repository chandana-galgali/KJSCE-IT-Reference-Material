from collections import Counter
from math import prod
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
frequency_map = Counter(A)
k = {}
result = []
for element, frequency in frequency_map.items():
    if frequency in k:
        k[frequency] += element
    else:
        k[frequency] = element      
freq_sorted = sorted(list(k.items()))
element_sum = list(map(prod, freq_sorted))
for i in range(Q):                      
    l, r = list(map(int, input().split()))    
    result.append(sum(element_sum[l-1 : r]))
for i in result:
    print(i)

'''from collections import Counter
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
frequency_map = Counter(A)
query_result = []
for _ in range(Q):
    l, r = map(int, input().split())
    sum = 0
    for element, frequency in frequency_map.items():
        if l <= frequency <= r:
            sum += element * frequency
    query_result.append(sum)
for _ in query_result:
    print(_)'''