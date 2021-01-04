def isIn(i,j):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False

def dfs(i,j,k):
    for d in range(4):
        ni = i+di[d]
        nj = j+dj[d]
        if(isIn(ni,nj) and not visit[ni][nj] and board[ni][nj]):
            visit[ni][nj] = True
            tmp[k] += 1
            dfs(ni,nj,k)
    
N = int(input())
board = []
visit = []
for _ in range(N):
    board.append(list(map(int,input())))
    visit.append([False]*N)

di = [0,0,-1,1]
dj = [-1,1,0,0]

tmp = []
k = -1
for i in range(N):
    for j in range(N):
        if(board[i][j] and not visit[i][j]):
            visit[i][j]=True
            tmp = tmp+[1]
            k = k+1
            dfs(i,j,k)
            
print(len(tmp))
tmp.sort()
for i in range(len(tmp)):
    print(tmp[i])