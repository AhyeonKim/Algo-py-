def comb(tmp,n):
    if len(tmp)==M:
        print(*tmp)
        return
    for i in range(n,N):
        comb(tmp+[arr[i]],i)
N,M = map(int,input().split())
arr = sorted(map(int,input().split()))
visit = [False]*N
comb([],0)