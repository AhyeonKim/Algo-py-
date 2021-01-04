from collections import deque

def isOut(i,j):
    if 0<=i<N and 0<=j<M:
        return False
    else: return True

M,N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]

di = [-1,0,0,1]
dj = [0,-1,1,0]
tomato = deque([])

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append([i,j,0])
while tomato:
    i, j, day = tomato.popleft()
    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        if(not isOut(ni,nj) and box[ni][nj]==0):
            tomato.append([ni,nj,day+1])
            box[ni][nj] = 1
# for i in box:
#     print(i)

for i in range(N):
    for j in range(M):
        if not box[i][j]:
            day = -1
print(day)
# boundary 체크
# visit