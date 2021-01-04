import copy
def isIn(i,j):
    if 0<=i<4 and 0<=j<4:
        return True
    else:
        return False
def solve(board,fish,si,sj,sum):
    global result
    cboard = copy.deepcopy(board)
    cfish = copy.deepcopy(fish)
    #eat
    sum += cboard[si][sj]
    result = max(result,sum)
    fish_num = cboard[si][sj]
    shark_dir = cfish[fish_num][1]
    cfish[fish_num] = [(-1,-1),-1]
    cboard[si][sj] = -1
    #fish move
    for f in range(1,17):
        if cfish[f][1]==-1:
            continue
        ci,cj = cfish[f][0]
        cd = cfish[f][1]
        ni, nj = ci+di[cd], cj+dj[cd]
        nd = cd
        while (ni==si and nj==sj) or not isIn(ni,nj):
            nd = (nd+1)%8
            ni, nj = ci+di[nd], cj+dj[nd]
        target = cboard[ni][nj]
        if target!=-1:
            cfish[target][0] = (ci,cj)
        cfish[f] = [(ni,nj),nd]
        cboard[ni][nj] = f
        cboard[ci][cj] = target
    #shark move
    for k in range(1,4):
        nsi = si+di[shark_dir]*k
        nsj = sj+dj[shark_dir]*k
        if isIn(nsi,nsj) and cboard[nsi][nsj]!=-1:
            solve(cboard,cfish,nsi,nsj,sum)


board = []
fish = {}
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,-1,-1,-1,0,1,1,1]
result = 0
for i in range(4):
    row = list(map(int,input().split()))
    board.append([0]*4)
    for j in range(4):
        num = row[2*j]
        dir = row[2*j+1]
        fish[num] = [(i,j),dir-1]
        board[i][j] = num
sum = 0
solve(board,fish,0,0,sum)
print(result)