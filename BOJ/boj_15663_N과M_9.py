def comb(tmp):
    if len(tmp)==M:
        if tuple(tmp) not in group:
            group.add(tuple(tmp))
            print(*tmp)
            return
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            comb(tmp+[arr[i]])
            visit[i] = False
N,M = map(int,input().split())
arr = sorted(map(int,input().split()))
visit = [False]*N
group = set()
comb([])