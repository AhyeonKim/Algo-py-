from collections import deque
def isIn(i,j):
    if 0<=i<N and 0<=j<M:
        return True
    else: return False
def bfs(q):
    block = 0
    while q:
        block += 1
        for _ in range(len(q)):
            now = q.popleft()
            if now[0]==N-1 and now[1]==M-1:
                return block
            for d in range(4):
                ni = now[0]+di[d]
                nj = now[1]+dj[d]
                if isIn(ni,nj) and not visit[ni][nj] and arr[ni][nj]==1:
                    visit[ni][nj] = True
                    q.append([ni,nj])
N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input())))
visit = [[False]*M for _ in range(N)]
di = [0,-1,0,1]
dj = [-1,0,1,0]
answer = bfs(deque([[0,0]]))
print(answer)