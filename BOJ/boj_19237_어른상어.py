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
priority = {}
for i in range(1,M+1):
    priority[i] = []
    for _ in range(4):
        priority[i].append(list(map(lambda x:x-1,map(int,input().split()))))
smell = [[False for _ in range(N)] for _ in range(N)]
t = 0
while t<=1000:
    for s in shark:
        smell[shark[s][0]][shark[s][1]]=[s,k]
    t+=1
    #shark move
    tmp = {}
    for s in shark:
        next = None
        si,sj,sd = shark[s]
        for d in range(4):
            nd = priority[s][sd][d]
            ni,nj = si+di[nd],sj+dj[nd]
            if -1<ni<N and -1<nj<N:
                if not smell[ni][nj]:
                    if (ni,nj) in tmp:
                        cur_s, cur_d = tmp[(ni,nj)]
                        if cur_s>s:
                            tmp[(ni,nj)] = (s,nd)
                    else:
                        tmp[(ni,nj)] = (s,nd)
                    break
                elif s==smell[ni][nj][0] and not next:
                    next = [ni,nj,nd]
        else:
            if (next[0],next[1]) in tmp:
                cur_s, cur_d = tmp[(next[0],next[1])]
                if cur_s>s:
                    tmp[(next[0],next[1])] = (s,next[2])
            else:
                tmp[(next[0],next[1])] = (s,next[2])
    shark = {}
    for (i,j) in tmp:
        n,d = tmp[(i,j)]
        shark[n] = [i,j,d]
    if len(shark)==1:
        break
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                smell[i][j][1]-=1
                if smell[i][j][1]==0:
                    smell[i][j]=False
if t>1000:
    print(-1)
else:
    print(t)