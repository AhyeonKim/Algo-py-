import sys
input = sys.stdin.readline
def move(h):
    global info, horses, flag
    i,j,d=horses[h]
    ni,nj = i+di[d],j+dj[d]
    if -1<ni<N and -1<nj<N:
        color = board[ni][nj]
    else:
        color = 2
    if color==0 or color==1:
        idx = info[i][j].index(h)
        tmp = info[i][j][idx:]
        info[i][j] = info[i][j][:idx]
        if color==1:
            tmp.reverse()
        for t in tmp:
            info[ni][nj].append(t)
            if len(info[ni][nj])>=4:
                flag=False
                return
            horses[t][0],horses[t][1] = ni,nj
    else:
        d = change_d[d]
        ni = i+di[d]
        nj = j+dj[d]
        horses[h][2] = d
        if -1<ni<N and -1<nj<N:
            if board[ni][nj]!=2:
                move(h)
di, dj = [0,0,0,-1,1],[0,1,-1,0,0]
change_d = {1:2,2:1,3:4,4:3}
N, K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
horses = []
info = [[[] for _ in range(N)] for _ in range(N)]
for k in range(K):
    i,j,d = map(int,input().split())
    horses.append([i-1,j-1,d])
    info[i-1][j-1].append(k)
turn = 0
flag = True
while turn<=1000:
    turn+=1
    for h in range(len(horses)):
        move(h)
        if not flag:
            break
    if not flag:
        break
if turn>1000:
    print(-1)
else:
    print(turn)