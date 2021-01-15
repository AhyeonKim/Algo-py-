from collections import deque
def bfs(q):
    while q:
        x,y = q.popleft()
        if (x,y) == store[n+1]:
            return "happy"
        for i in range(1,n+2):
            if not visit[i]:
                x1,y1 = store[i]
                if abs(x1-x)+abs(y1-y)<=1000:
                    visit[i]=True
                    q.append(store[i])
    return "sad"

t = int(input())
for _ in range(t):
    n = int(input())
    store = []
    for _ in range(n+2):
        a,b = map(int,input().split())
        store.append((a,b))
    visit = [False]*(n+2)
    visit[0] = True
    ans = bfs(deque([store[0]]))
    print(ans)
    