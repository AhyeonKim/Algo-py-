import sys
input = sys.stdin.readline
def distance(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)
def choice(idx,chicken):
    global stores,answer
    if len(chicken)+len(stores)-idx<M:
        return
    if len(chicken)==M:
        chicken_d = 0
        for home in homes:
            y,x = home
            d = sys.maxsize
            for c in chicken:
                cy,cx = c
                d = min(d,distance(y,x,cy,cx))
            chicken_d += d
        answer = min(chicken_d,answer)
        return
    i,j = stores[idx]
    board[i][j] = 3
    choice(idx+1,chicken+[stores[idx]])
    board[i][j] = 2
    choice(idx+1,chicken)
    
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
di, dj = [0,-1,0,1], [-1,0,1,0]
answer = sys.maxsize
stores = []
homes = []
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            homes.append((i,j))
        elif board[i][j]==2:
            stores.append((i,j))
choice(0,[])
print(answer)