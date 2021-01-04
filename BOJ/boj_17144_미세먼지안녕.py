def canmove(i,j):
    if 0<=i<R and 0<=j<C and board[i][j]!=-1:
        return True
    else:
        return False
def dust():
    global board
    tmp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0 and board[i][j] != -1:
                k = board[i][j]//5
                cnt = 0
                for d in range(4):
                    ni, nj = i+di[d], j+dj[d]
                    if(canmove(ni,nj)):
                        tmp[ni][nj] += k
                        cnt += 1
                tmp[i][j] = tmp[i][j] + (k*cnt*-1)
    for i in range(R):
        for j in range(C):
            board[i][j] += tmp[i][j]

def clean():
    global board
    x = cleaner
    for i in range(x-1,0,-1):
        board[i][0], board[i-1][0] = board[i-1][0],0
    for j in range(C-1):
        board[0][j], board[0][j+1] = board[0][j+1],0
    for i in range(x):
        board[i][C-1], board[i+1][C-1]= board[i+1][C-1],0
    for j in range(C-1,1,-1):
        board[x][j], board[x][j-1] = board[x][j-1],0
    x = cleaner+1
    for i in range(x+1,R-1,1):
        board[i][0], board[i+1][0] = board[i+1][0], 0
    for j in range(C-1):
        board[R-1][j], board[R-1][j+1] = board[R-1][j+1],0
    for i in range(R-1,x,-1):
        board[i][C-1], board[i-1][C-1] = board[i-1][C-1],0
    for j in range(C-1,1,-1):
        board[x][j], board[x][j-1] = board[x][j-1],0

R,C,T = map(int,input().split())    
board = []
for r in range(R):
    board.append(list(map(int,input().split())))

cleaner = 0
for i in range(R):
    if board[i][0] == -1:
        cleaner = i
        break

di, dj = [0,0,1,-1],[1,-1,0,0]

for _ in range(T):
    dust()
    clean()
answer = 0
for b in board:
    for i in b:
        answer += i

answer = answer+2
print(answer)