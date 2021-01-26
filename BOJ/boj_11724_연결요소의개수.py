import sys
input = sys.stdin.readline
N, M = map(int,input().split())
link = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    link[u].append(v)
    link[v].append(u)
visit = [False]*(N+1)
answer=0
for i in range(1,N+1):
    if not visit[i]:
        answer+=1
        visit[i] = True
        q=[i]
        while q:
            for _ in range(len(q)):
                n = q.pop()
                for j in link[n]:
                    if not visit[j]:
                        visit[j] = True
                        q.append(j)
print(answer)