import sys
sys.setrecursionlimit(10**6)
def comb(tmp):
    if len(tmp)==M:
        if tuple(tmp) not in group:
            group.add(tuple(tmp))
            print(*tmp)
        return
    for i in range(N):
        comb(tmp+[arr[i]])
N,M = map(int,input().split())
arr = sorted(map(int,input().split()))
group = set()
comb([])