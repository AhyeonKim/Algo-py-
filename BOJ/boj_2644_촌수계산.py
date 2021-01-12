from collections import deque
def bfs(q):
    step = 0
    while q:
        print(q)
        step+=1
        for _ in range(len(q)):
            t = q.popleft()
            visit[t] = True
            for i in arr[t]:
                if i==b:
                    return step
                if not visit[i]:
                    q.append(i)
    return -1
N = int(input())
a, b = map(int,input().split())
m = int(input())
arr = [[] for _ in range(N+1)]
visit = [False]*(N+1)
for _ in range(m):
    x, y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
visit[a] = True
flag = False
answer = bfs(deque([a]))
print(answer)