N = int(input())
link = int(input())
connect = [[False]*(N+1) for _ in range(N+1)]
visit = [False]*(N+1)
for _ in range(link):
    a, b = map(int,input().split())
    connect[a][b] = True
    connect[b][a] = True
queue = [1]
queue.append(1)
while queue:
    i = queue.pop(0)
    for j in range(2,N+1):
        if connect[i][j] and not visit[j]:
            queue.append(j)
            visit[j] = True
print(sum(visit))