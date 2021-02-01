M,N = map(int,input().split())
arr = [False]*2+[True]*(N-1)
for i in range(2,N+1):
    if arr[i]:
        for j in range(i*2,N+1,i):
            arr[j] = False
for i in range(M,N+1):
    if arr[i]:
        print(i)