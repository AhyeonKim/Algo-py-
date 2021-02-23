import sys
from collections import deque
def bfs(q):
    while q:
        i,j,cnt,flag = q.popleft()
        if i==N-1 and j==M-1:
            return cnt
        for d in range(4):
            ni,nj = i+di[d],j+dj[d]
            if -1<ni<N and -1<nj<M:
                # flag 있는데 안뿌시고갈때
                if not arr[ni][nj] and not broken[ni][nj] and not flag:
                    broken[ni][nj]=True
                    visit[ni][nj]=True
                    q.append((ni,nj,cnt+1,flag))
                # 뿌셔야할때
                elif arr[ni][nj] and not broken[ni][nj] and not flag:
                    broken[ni][nj]=True
                    q.append((ni,nj,cnt+1,True))
                # 뿌시는거 없을때
                elif not arr[ni][nj] and not visit[ni][nj]:
                    visit[ni][nj]=True
                    q.append((ni,nj,cnt+1,flag))
    return -1
input=sys.stdin.readline
N,M = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().strip())))
di,dj=[0,-1,0,1],[-1,0,1,0]
visit = [[False]*M for _ in range(N)]
broken= [[False]*M for _ in range(N)]
visit[0][0] = True
broken[0][0] = True
ans = bfs(deque([(0,0,1,False)]))
print(ans)