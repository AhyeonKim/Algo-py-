import heapq
def solution(n, costs):
    visit = set([])
    answer = 0
    nodes = [[] for _ in range(n)]
    for c in costs:
        u,v,w = c
        nodes[u].append((w,v))
        nodes[v].append((w,u))
    tmp = [(0,0)]
    while tmp:
        value, current = heapq.heappop(tmp)
        if current not in visit:
            answer+=value
            visit.add(current)
            if len(visit)==n:
                break
            for (w,v) in nodes[current]:
                heapq.heappush(tmp,(w,v))
    return answer