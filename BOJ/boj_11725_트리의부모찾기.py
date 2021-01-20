import sys
input=sys.stdin.readline
N = int(input())
V = [[] for _ in range(N+1)]
for _ in range(N-1):
    v,w = map(int,input().split())
    V[v].append(w)
    V[w].append(v)
parent = [True]*2+[False]*(N-1)
q = []
for i in V[1]:
    parent[i]=1
    q.append(i)
while q:
    for _ in range(len(q)):
        tmp = q.pop()
        for i in V[tmp]:
            if not parent[i]:
                parent[i] = tmp
                q.append(i)
for p in parent[2:]:
    print(p)