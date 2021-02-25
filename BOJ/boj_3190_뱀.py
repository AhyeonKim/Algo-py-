N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
board[0][0]=1
for _ in range(K):
    i,j = map(int,input().split())
    board[i][j]=-1
L = int(input())
info=[]
for _ in range(L):
    x,c = input().split()
    info.append((int(x),c))
