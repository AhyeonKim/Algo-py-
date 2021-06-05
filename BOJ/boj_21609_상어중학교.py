from collections import deque
import sys
input = sys.stdin.readline
def down():
    global board,N
    for j in range(N):
        for i in range(N-1,-1,-1):
            if board[i][j]!=-1:
                ci=i+1
                while True:
                    if ci==N:
                        break
                    if board[ci][j]==-2:
                        ci+=1
                    else:
                        break
                if board[ci-1][j]==-2:
                    board[ci-1][j]=board[i][j]
                    board[i][j]=-2
    # for i in range(N):
    #     for y in range(N-i-1):
    #         for x in range(N):
    #             if board[y][x] > -1 and board[y+1][x] == -2:
    #                 board[y][x],board[y+1][x] = board[y+1][x],board[y][x]
di, dj = [-1,0,1,0],[0,-1,0,1]
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer = 0
while True:
    #step1
    blocks = []
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and board[i][j]>0:
                color = board[i][j]
                visit[i][j] = True
                cnt = 1
                q = deque([(i,j)])
                ii,jj = i,j
                rainbows = []
                while q:
                    ci,cj = q.popleft()
                    for d in range(4):
                        ni,nj = ci+di[d],cj+dj[d]
                        if -1<ni<N and -1<nj<N and not visit[ni][nj]:
                            if board[ni][nj]==0 or board[ni][nj]==color:
                                cnt+=1
                                if board[ni][nj]==0:
                                    rainbows.append((ni,nj))
                                else:
                                    if ni<ii:
                                        ii = ni
                                        jj = nj
                                    elif ni==ii:
                                        if nj<jj:
                                            jj = nj
                                visit[ni][nj]=True
                                q.append((ni,nj))
                if cnt>=2:
                    blocks.append((cnt,len(rainbows),ii,jj))
                for ri,rj in rainbows:
                    visit[ri][rj]=False
    if not blocks:
        break
    blocks.sort(reverse=True)
    block = blocks[0]
    #step2
    c,r,ci,cj = block
    q = deque([(ci,cj)])
    answer += c*c
    visit = [[False]*N for _ in range(N)]
    visit[ci][cj]=True
    color = board[ci][cj]
    board[ci][cj]=-2
    while q:
        ci,cj = q.popleft()
        for d in range(4):
            ni,nj = ci+di[d],cj+dj[d]
            if -1<ni<N and -1<nj<N and not visit[ni][nj]:
                if board[ni][nj]==0 or board[ni][nj]==color:
                    visit[ni][nj]=True
                    q.append((ni,nj))
                    board[ni][nj]=-2
    down()
    n_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            n_board[i][j] = board[j][N-i-1]
    board = n_board
    down()
print(answer)