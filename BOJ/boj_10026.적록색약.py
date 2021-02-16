di,dj = [0,-1,0,1],[-1,0,1,0]
def check(q,c):
    while(q):
        tmp_i, tmp_j = q.pop()
        for d in range(4):
            ni,nj = tmp_i+di[d], tmp_j+dj[d]
            if -1<ni<N and -1<nj<N and not visit[ni][nj] and arr[ni][nj]==c:
                visit[ni][nj] = True
                q.append((ni,nj))
def check2(q,c):
    while(q):
        tmp_i, tmp_j = q.pop()
        for d in range(4):
            ni,nj = tmp_i+di[d], tmp_j+dj[d]
            if -1<ni<N and -1<nj<N and not visit[ni][nj]:
                if (c=='B' and arr[ni][nj]=='B') or (c!='B' and arr[ni][nj]!='B'):
                    visit[ni][nj] = True
                    q.append((ni,nj))
N = int(input())
arr = []
for _ in range(N):
    arr.append(input())
p1,p2=0,0
visit = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            p1+=1
            check([(i,j)],arr[i][j])
visit = [[False]*N for _ in range(N)]        
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            p2+=1
            check2([(i,j)],arr[i][j])
print(p1,p2)