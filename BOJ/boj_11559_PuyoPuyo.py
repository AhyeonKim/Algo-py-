board = []
for _ in range(12):
    board.append(list(input()))
answer = 0
di,dj = [-1,0,1,0],[0,1,0,-1]
while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if board[i][j]!='.':
                color = board[i][j]
                cnt = 1
                q = [(i,j)]
                tmp = [(i,j)]
                visit = [[False]*6 for _ in range(12)]
                visit[i][j]=True
                while q:
                    ci, cj = q.pop()
                    for d in range(4):
                        ni,nj = ci+di[d],cj+dj[d]
                        if -1<ni<12 and -1<nj<6 and not visit[ni][nj] and board[ni][nj]==color:
                            cnt+=1
                            visit[ni][nj]=True
                            q.append((ni,nj))
                            tmp.append((ni,nj))
                if cnt>=4:
                    flag = True
                    for y,x in tmp:
                        board[y][x]='.'
    for jj in range(6):
        for ii in range(10,-1,-1):
            if board[ii]+[jj]!='.':
                pii=ii
                nii=ii+1
                while nii<12:
                    if board[nii][jj]=='.':
                        board[nii][jj]=board[pii][jj]
                        board[pii][jj]='.'
                    pii=nii
                    nii+=1
    if not flag:
        break
    else:
        answer+=1
print(answer)