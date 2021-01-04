def back(tmp):
    if len(tmp)==M:
        print(*tmp)
    else:
        for i in range(N):
            if visit[i]==False:
                visit[i] = True
                back(tmp+[i+1])
                visit[i] = False

N,M = map(int,input().split())
visit = [False] * N
back([])
