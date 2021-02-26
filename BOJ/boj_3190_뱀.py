import sys
def isIn(i,j):
    return -1<i<N and -1<j<N
input=sys.stdin.readline
N = int(input())
K = int(input())
move = [[0,-1],[-1,0],[0,1],[1,0]] # L(0),U(1),R(2),D(3)
board = [[-1]*N for _ in range(N)]
board[0][0]=2
for _ in range(K):
    i,j = map(int,input().split())
    board[i][j]=4 # 사과
L = int(input())
info=[]
for _ in range(L):
    x,c = input().split()
    info.append([int(x),c])
head=[0,0]
tail=[0,0]
t=0
while True:
    d = board[head[0]][head[1]]
    if info and info[0][0]==t:
        tmp = info[0][1]
        info.pop(0)
        if tmp=='L':
            d=0
        elif tmp=='U':
            d=1
        elif tmp=='R':
            d=2
        elif tmp=='D':
            d=3

    ni,nj = head[0]+move[d][0], head[1]+move[d][1]
    
    if not isIn(ni,nj) or -1<board[ni][nj]<4:
        break
    if board[ni][nj]!=4:
        td = board[tail[0]][tail[1]]
        board[tail[0]][tail[1]]=-1
        tail[0],tail[1] = tail[0]+move[td][0], tail[1]+move[td][1]
    head = [ni,nj]
    board[ni][nj] = d
    t+=1
print(t)