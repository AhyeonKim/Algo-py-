import sys
input = sys.stdin.readline
di,dj = [0,-1,0,1],[-1,0,1,0]
cctv = {
    1:[[0],[1],[2],[3]],
    2:[[1,3],[0,2]],
    3:[[0,1],[1,2],[2,3],[3,0]],
    4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5:[[0,1,2,3]]
}
def isIn(i,j):
    return -1<i<N and -1<j<M
def check(idx,cnt):
    global board,candi
    if idx==len(cameras):
        candi=max(candi,cnt)
        return
    else:
        i,j,num = cameras[idx]
        for dd in cctv[num]:
            tmp=[]
            for d in dd:
                ni = i+di[d]
                nj = j+dj[d]
                while isIn(ni,nj) and board[ni][nj]!=6:
                    if not board[ni][nj]:
                        tmp.append((ni,nj))
                    ni+=di[d]
                    nj+=dj[d]
            for y,x in tmp:
                board[y][x]='#'
            check(idx+1,cnt+len(tmp))
            for y,x in tmp:
                board[y][x]=0
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer=N*M
cameras = []
for i in range(N):
    for j in range(M):
        if board[i][j]:
            answer-=1
            if board[i][j]!=6:
                cameras.append((i,j,board[i][j]))
candi=0
check(0,0)
answer -= candi
print(answer)