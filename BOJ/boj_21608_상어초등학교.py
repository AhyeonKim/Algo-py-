N = int(input())
wants = {}
board = [[0]*N for _ in range(N)]
di, dj = [-1,1,0,0],[0,0,-1,1]
for _ in range(N*N):
    tmp = list(map(int,input().split()))
    student = tmp[0]
    wants[student] = tmp[1:]
    candi = []
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                blank, friend = 0,0
                for d in range(4):
                    ni,nj = i+di[d],j+dj[d]
                    if -1<ni<N and -1<nj<N:
                        if not board[ni][nj]:
                            blank+=1
                        elif board[ni][nj] in wants[student]:
                            friend+=1
                candi.append((friend,blank,-i,-j))
    candi.sort(reverse=True)
    board[candi[0][2]*-1][candi[0][3]*-1]=student
ans = 0
satisfy = {0:0,1:1,2:10,3:100,4:1000}
for i in range(N):
    for j in range(N):
        s = board[i][j]
        cnt = 0
        for d in range(4):
            ni,nj = i+di[d],j+dj[d]
            if -1<ni<N and -1<nj<N:
                if board[ni][nj] in wants[s]:
                    cnt+=1
        ans+=satisfy[cnt]
print(ans)