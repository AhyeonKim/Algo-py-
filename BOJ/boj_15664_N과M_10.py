def comb(tmp,n):
    if len(tmp)==M:
        if tuple(tmp) not in group:
            group.add(tuple(tmp))
            print(*tmp)
        return
    for i in range(n,N):
        comb(tmp+[arr[i]],i+1)
N,M = map(int,input().split())
arr = sorted(map(int,input().split()))
group = set()
comb([],0)