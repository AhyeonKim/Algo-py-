from collections import deque
dh = [-1,1,0,0,0,0]
di = [0,0,0,-1,0,1]
dj = [0,0,-1,0,1,0]
def bfs(q):
    step = 0
    while q:
        step+=1
        for _ in range(len(q)):
            now = q.popleft()
            for d in range(6):
                nh = now[0]+dh[d]
                ni = now[1]+di[d]
                nj = now[2]+dj[d]
                if 0<=nh<H and 0<=ni<N and 0<=nj<M:
                    if tomato[nh][ni][nj]==0:
                        tomato[nh][ni][nj]=1
                        q.append([nh,ni,nj])
    return step-1
M,N,H = map(int,input().split())
tomato = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int,input().split())))
    tomato.append(tmp)
q = deque([])
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j]==1:
                q.append([h,i,j])
ans = bfs(q)
flag = False
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j]==0:
                flag = True
                break
print(ans if not flag else -1)