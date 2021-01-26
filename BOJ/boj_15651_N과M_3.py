def comb(tmp):
    if len(tmp)==M:
        print(*tmp)
        return
    for i in range(1,N+1):
        tmp.append(i)
        comb(tmp)
        tmp.pop()
N,M = map(int,input().split())
comb([])