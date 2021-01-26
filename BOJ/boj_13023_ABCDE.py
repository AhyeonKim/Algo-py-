import sys
sys.setrecursionlimit(10**6)
def dfs(i,cnt):
    global flag
    if cnt==4:
        flag = True
    if not flag:
        visit[i] = True
        for j in link[i]:
            if not visit[j]:
                dfs(j,cnt+1)
        visit[i] = False
N,M = map(int,input().split())
link = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
flag = False
for i in range(N):
    visit = [False]*N
    dfs(i,0)
    if flag:
        break
print(1 if flag else 0)