import sys
input = sys.stdin.readline
di, dj = [-1,1,0,0], [0,0,-1,1]
N,M,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
shark = {}
for i in range(N):
    for j in range(N):
        if board[i][j]:
            shark[board[i][j]] = [i,j]
s_d = list(map(int,input().split()))
for i in range(len(s_d)):
    shark[i+1].append(s_d[i]-1)
print(shark)
priority = {}
for i in range(M):
    priority[i] = []
    for _ in range(4):
        priority[i].append(list(map(lambda x:x-1,map(int,input().split()))))
print(priority)
smell = [[False for _ in range(N)] for _ in range(N)]
t = 0
while t<=1000:
    for s in shark:
        smell[shark[s][0]][shark[s][1]]=[s,k]
    t+=1
    #shark move
    for s in shark:
        next = [0,0,0]
        si,sj,sd = s
        for d in range(4):
            tmp = []
            nd = priority[s][sd][d]
            ni,nj = si+di[nd],sj+dj[nd]
            if not smell[ni][nj]:
                shark[s] = [ni,nj,nd]
                break
            elif s==smell[ni][nj][0]:
                next = [ni,nj,nd]
        else:
            shark[s] = next


if t>1000:
    print(-1)
else:
    print(t)