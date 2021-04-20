import sys
from collections import deque
input = sys.stdin.readline
def choice(idx,alive):
    global answer
    if len(alive)+len(virus)-idx<M:
        return
    if len(alive)==M:
        q = deque(alive)
        t = 0
        z = 0
        visit = [[False]*N for _ in range(N)]
        while q and zeros!=z:
            t+=1
            for _ in range(len(q)):
                i,j = q.popleft()
                for d in range(4):
                    ni,nj = i+di[d], j+dj[d]
                    if -1<ni<N and -1<nj<N and not visit[ni][nj]:
                        if board[ni][nj]==0 or board[ni][nj]=='*':
                            visit[ni][nj] = True
                            if board[ni][nj]==0:
                                z+=1
                            q.append((ni,nj))
        if zeros==z:
            answer = min(answer,t)
    else:
        y,x = virus[idx]
        board[y][x]='#'
        choice(idx+1,alive+[(y,x)])
        board[y][x]='*'
        choice(idx+1,alive)
    
di, dj = [-1,1,0,0], [0,0,-1,1]
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer = sys.maxsize
virus = []
zeros = 0
for i in range(N):
    for j in range(N):
        if board[i][j]==0:
            zeros += 1
        elif board[i][j]==1:
            board[i][j]='-'
        elif board[i][j]==2:
            virus.append((i,j))
            board[i][j]='*'
choice(0,[])
if answer==sys.maxsize:
    print(-1)
else:
    print(answer)