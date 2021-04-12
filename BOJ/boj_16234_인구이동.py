import sys
from collections import deque
sys.setrecursionlimit(10**6)

def isIn(i,j):
    return 0<=i<N and 0<=j<N

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
                    for i,j in tmp:
                        value = total//cnt
                        ground[i][j] = value
    if flag:
        ans+=1
print(ans)