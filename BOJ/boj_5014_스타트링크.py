from collections import deque
def bfs(q):
    count = -1
    while q:
        count +=1
        for _ in range(len(q)):
            tmp = q.popleft()
            if tmp==G:
                return count
            for x in [tmp-D, tmp+U]:
                if 1<=x<=F and not visit[x]:
                    visit[x] = True
                    q.append(x)
    return "use the stairs"
F,S,G,U,D = map(int,input().split())
visit = [False]*(F+1)
visit[S] = True
ans = bfs(deque([S]))
print(ans)