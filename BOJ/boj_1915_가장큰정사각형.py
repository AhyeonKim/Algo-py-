import sys
input = sys.stdin.readline
n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().strip())))
max_size = 0
for j in range(m):
    if board[0][j]==1:
        max_size=1
        break
if max_size==0:
    for i in range(n):
        if board[i][0]==1:
            max_size=1
            break
for i in range(1,n):
    for j in range(1,m):
        if board[i][j]!=0:
            tmp = min(board[i-1][j-1], board[i-1][j], board[i][j-1])
            board[i][j] += tmp
            max_size = max(max_size,board[i][j])
print(max_size*max_size)