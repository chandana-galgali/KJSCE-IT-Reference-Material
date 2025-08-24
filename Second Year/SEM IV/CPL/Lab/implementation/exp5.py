def computeLPSArray(P):
    m = len(P)
    lps = [0] * m
    l = 0
    i = 1
    while i < m:
        if P[i] == P[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i += 1
    return lps
def KMPSearch(P, T):
    M = len(P)
    N = len(T)
    lps = computeLPSArray(P)
    i = j = 0
    count = 0
    while i < N:
        if P[j] == T[i]:
            i += 1
            j += 1
        if j == M:
            count += 1
            j = lps[j-1]
        elif i < N and P[j] != T[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return count
P = input()
T = input()
result = KMPSearch(P, T)
print(result)

# P = "sda"
# T = "sadasda"