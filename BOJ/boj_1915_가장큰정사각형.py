import sys
input = sys.stdin.readline
def check(i,j,m):
    size = m
    while True:
        tmp = size+1
        if i+tmp<=n and j+tmp<=m:
            for k1 in range(tmp):
                ni = i+k1
                for k2 in range(tmp):
                    nj = j+k2
                    if board[ni][nj]!=1:
                        return size
        else: return size
        size = tmp
n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().strip())))
max_size = 0
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            max_size = check(i,j,max_size)
print(max_size*max_size)
