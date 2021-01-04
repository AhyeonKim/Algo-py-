from collections import deque

def isIn(i,j):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

shark_size = 2
shark_eat = 0
shark = [0,0,0]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark[0] = i
            shark[1] = j
            board[i][j] = 0
            break

di = [-1,0,1,0]
dj = [0,-1,0,1]

is_update = True
while is_update:
    is_update = False
    visited = [[False]*N for _ in range(N)]
    visited[shark[0]][shark[1]] = True
    q = deque([shark])
    tmp = [20,0,-1]

    while q:
        cur = q.popleft()
        if tmp[2]!=-1 and tmp[2]<cur[2]:
            break
        if 0<board[cur[0]][cur[1]]<shark_size:
            is_update = True
            if tmp[0]>cur[0] or (tmp[0]==cur[0] and tmp[1]>cur[1]):
                tmp = cur

        for d in range(4):
            ni = cur[0]+di[d]
            nj = cur[1]+dj[d]
            nt = cur[2]+1
            if isIn(ni,nj)==False:
                continue
            if visited[ni][nj]==False and board[ni][nj]<=shark_size:
                visited[ni][nj] = True
                q.append([ni,nj,nt])

    if is_update:
        shark = tmp
        shark_eat += 1
        if shark_eat == shark_size:
            shark_size+=1
            shark_eat = 0
        board[shark[0]][shark[1]] = 0

print(shark[2])

