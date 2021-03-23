di,dj = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
N,M,K = map(int,input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    board[r-1][c-1].append((m,s,d))
for _ in range(K):
    tmp = {}
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                for m,s,d in board[i][j]:
                    ni, nj = (i+di[d]*s)%N, (j+dj[d]*s)%N
                    if (ni,nj) in tmp:
                        tmp[(ni,nj)].append((m,s,d))
                    else:
                        tmp[(ni,nj)]=[(m,s,d)]
                board[i][j]=[]

    for i,j in tmp:
        balls = tmp[(i,j)]
        if len(balls)>1:
            total_m, total_s, total_d = 0,0,0
            for m,s,d in balls:
                total_m+=m
                total_s+=s
                total_d+=d%2
            total_m//=5
            total_s//=len(balls)
            if total_m:
                for k in range(4):
                    if total_d in [0,len(balls)]:
                        d = 2*k
                    else:
                        d = 2*k+1
                    board[i][j].append((total_m,total_s,d))
        else:
            board[i][j]=balls
ans = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for m,s,d in board[i][j]:
                ans+=m
print(ans)