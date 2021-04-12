import sys
from collections import deque

def isIn(i,j):
    return -1<i<N and -1<j<N

N, L, R = map(int,input().split())
ground=[]
for _ in range(N):
    ground.append(list(map(int,input().split())))

di, dj = [0,-1,0,1], [-1,0,1,0]
ans = 0
flag = True
while flag:
    flag = False
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j] = True
                cnt = 1
                total = ground[i][j]
                tmp = [(i,j)]
                q = deque([(i,j)])
                while q:
                    ci, cj = q.popleft()
                    for d in range(4):
                        ni, nj = ci+di[d], cj+dj[d]
                        if isIn(ni,nj) and not visit[ni][nj] and L<=abs(ground[ci][cj]-ground[ni][nj])<=R:
                            visit[ni][nj] = True
                            cnt+=1
                            total+=ground[ni][nj]
                            tmp.append((ni,nj))
                            q.append((ni,nj))
                if cnt>1:
                    flag = True
                    for y,x in tmp:
                        value = total//cnt
                        ground[y][x] = value
    if flag:
        ans+=1
print(ans)