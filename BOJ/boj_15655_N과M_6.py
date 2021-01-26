def comb(tmp,n):
    if len(tmp)==M:
        print(*tmp)
        return
    for i in range(n,N):
        if not visit[i]:
            visit[i] = True
            comb(tmp+[arr[i]],i+1)
            visit[i] = False
N,M = map(int,input().split())
arr = sorted(map(int,input().split()))
visit = [False]*N
comb([],0)