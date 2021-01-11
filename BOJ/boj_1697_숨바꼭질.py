from collections import deque
N, K = map(int, input().split())
time = 0
queue = deque([[N,time]])
visit = [False]*100001
visit[N]=True
if K<N:
    print(N-K)
else:
    while queue:
        now, t = queue.popleft()
        visit[now]=True
        if now==K:
            time = t
            break
        t+=1
        for x in [now-1, now+1, now*2]:
            if 0<=x<=100000 and not visit[x]:
                queue.append([x,t])
    print(time)