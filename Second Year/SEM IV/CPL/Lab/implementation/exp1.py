N=int(input())
A=[]
A=list(map(int, input().split(" ")))
if(A[N-1]%10==0):
    print("Yes")
else:
    print("No")