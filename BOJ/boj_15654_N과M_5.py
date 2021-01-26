def comb(tmp):
    if len(tmp)==M:
        print(*tmp)
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            comb(tmp+[arr[i]])
            visit[i] = False
N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visit = [False]*(N)
comb([])