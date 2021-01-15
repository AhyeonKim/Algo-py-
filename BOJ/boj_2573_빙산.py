def check(q,visit):
    while q:
        i,j = q.pop()
        for d in range(4):
            ni = i+di[d]
            nj = j+dj[d]
            if isIn(ni,nj) and not visit[ni][nj] and ice[ni][nj]>0:
                visit[ni][nj]=True
                q.append((ni,nj))

def isIn(i,j):
    return -1<i<N and -1<j<M

def melt():
    year = 0
    while True:
        if sum(map(sum,ice))==0:
            return 0
        #덩어리 세기
        cnt = 0
        visit = [[False]*M for _ in range(N)]
        for i in range(1,N-1):
            for j in range(1,M-1):
                if ice[i][j] and not visit[i][j]:
                    cnt+=1
                    if cnt>1:
                        return year
                    visit[i][j] = True
                    check([(i,j)],visit)
        #빙산 얼마나 녹을지
        melt = [[0]*(M) for _ in range(N)]
        for i in range(1,N-1):
            for j in range(1,M-1):
                if ice[i][j]:
                    for d in range(4):
                        ni = i+di[d]
                        nj = j+dj[d]
                        if isIn(ni,nj) and not ice[ni][nj]:
                            melt[i][j]+=1
        #빙산 녹음
        for i in range(1,N-1):
            for j in range(1,M-1):
                ice[i][j] -= melt[i][j]
                if ice[i][j]<0:
                    ice[i][j]=0
        year+=1
    
N,M = map(int,input().split())
ice = []
for _ in range(N):
    ice.append(list(map(int,input().split())))
di, dj = [0,-1,0,1],[-1,0,1,0]
answer = melt()
print(answer)