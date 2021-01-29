def bfs(q,cnt):
    while q:
        i,j = q.pop()
        for d in range(4):
            ni,nj = i+di[d], j+dj[d]
            if -1<ni<N and -1<nj<M and not board[ni][nj]:
                q.append((ni,nj))
                board[ni][nj] = True
                cnt+=1
    area.append(cnt)

M,N,K = map(int,input().split())
board = [[False]*M for _ in range(N)]
for _ in range(K):
    si,sj,ei,ej = map(int,input().split())
    for i in range(si,ei):
        for j in range(sj,ej):
            board[i][j] = True
area = []
di, dj = [0,-1,0,1], [-1,0,1,0]
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            board[i][j] = True
            bfs([(i,j)],1)
print(len(area))
print(*sorted(area))