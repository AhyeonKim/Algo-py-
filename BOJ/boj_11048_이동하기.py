def isIn(i,j):
    return -1<i and -1<j
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
di, dj = [-1,-1,0], [-1,0,-1]
for i in range(N):
    for j in range(M):
        tmp=0
        for d in range(3):
            ni = i+di[d]
            nj = j+dj[d]
            if isIn(ni,nj) and board[ni][nj]>tmp:
                tmp = board[ni][nj]
        board[i][j]+=tmp
print(board[N-1][M-1])