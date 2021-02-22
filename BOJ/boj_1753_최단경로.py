import heapq
V,E = map(int,input().split())
K = int(input())
nodes = [[] for _ in range(V+1)]
INF = 10**8
prices=[INF] * (V+1)
prices[K] = 0
for _ in range(E):
    u,v,w = map(int,input().split())
    nodes[u].append((w,u,v))
heapq.heappush(tmp,nodes[K])
while tmp:
    value, current, next_node = heapq.heappop(tmp)
    if prices[next_node] > prices[current] + value:
        prices[next_node] = prices[current] + value
        for node in nodes[next_node]:
            heapq.heappush(tmp,node)
for i in range(1,V+1):
    if prices[i]==INF:
        print('INF')
    else: print(prices[i])

