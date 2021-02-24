import sys
import heapq
input=sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())
nodes = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,c = map(int,input().split())
    nodes[s].append((e,c))
A,B = map(int,input().split())
prices = [INF]*(N+1)
prices[A]=0
tmp = [(0,A)]
while tmp:
    value,current = heapq.heappop(tmp)
    for e,c in nodes[current]:
        if prices[e]<c:
            continue
        if prices[current]+c<prices[e]:
            prices[e]=prices[current]+c
            heapq.heappush(tmp,(prices[e],e))
print(prices[B])