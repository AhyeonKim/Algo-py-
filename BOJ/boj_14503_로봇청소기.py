def isIn(i,j):
    if 0<=i<N and 0<=j<M:
        return True
    else:
        return False

def robot(r,c,d):
    global answer
    if board[r][c]==0:
        answer += 1
        board[r][c] = 2
    for i in range(4):
        dd = (d+3-i)%4
        rr = r+di[dd]
        cc = c+dj[dd]
        if isIn(rr,cc) and board[rr][cc]==0:
            robot(rr,cc,dd)
            return
    rr = r+di[(d+2)%4]
    cc = c+dj[(d+2)%4]
    if isIn(rr,cc) and board[rr][cc]!=1:
        robot(rr,cc,d)
    else:
        return

N, M = list(map(int,input().split()))
r, c, d = list(map(int,input().split()))
board = []
di = [-1,0,1,0]
dj = [0,1,0,-1]
for _ in range(N):
    board.append(list(map(int,input().split())))

answer = 0
robot(r,c,d)
print(answer)