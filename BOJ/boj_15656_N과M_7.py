def comb(tmp):
    if len(tmp)==M:
        print(*tmp)
        return
    for i in range(N):
        comb(tmp+[arr[i]])
N,M = map(int,input().split())
arr = sorted(map(int,input().split()))
comb([])