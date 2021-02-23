import heapq
import sys
input = sys.stdin.readline
V,E = map(int,input().split())
K = int(input())
nodes = [[] for _ in range(V+1)]
INF = 10**8
prices=[INF] * (V+1)
prices[K] = 0
for _ in range(E):
    u,v,w = map(int,input().split())
    nodes[u].append((w,v))
tmp = [(0,K)]
while tmp:
    value, current = heapq.heappop(tmp)
    for (w,v) in nodes[current]:
        if prices[current] + w < prices[v]:
            prices[v] = prices[current] + w
            heapq.heappush(tmp,(prices[v],v))
for i in range(1,V+1):
    if prices[i]==INF:
        print('INF')
    else: print(prices[i])