from collections import deque
def dfs(V):
    visit[V] = True
    dfs_answer.append(V)
    for i in range(1,N+1):
        if not visit[i] and arr[V][i]:
            dfs(i)
    return

def bfs(V):
    visit[V] = True
    tmp = deque([])
    tmp.append(V)
    while tmp:
        v = tmp.popleft()
        bfs_answer.append(v)
        for i in range(1,N+1):
            if not visit[i] and arr[v][i]:
                visit[i] = True
                tmp.append(i)
    return

N,M,V = map(int,input().split())

arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    arr[s][e] = 1
    arr[e][s] = 1
dfs_answer = []
visit = [False] * (N+1)
dfs(V)

bfs_answer = []
visit = [False] * (N+1)
bfs(V)

print(*dfs_answer)
print(*bfs_answer)
