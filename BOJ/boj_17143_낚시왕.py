import sys
input = sys.stdin.readline
next_d = {1:2,2:1,3:4,4:3}
di,dj = [0,-1,1,0,0],[0,0,0,1,-1]
R,C,M = map(int,input().split())
board = [[False for _ in range(C)]for _ in range(R)]
ans = 0
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    board[r-1][c-1] = (s,d,z)
for king in range(C):
    for i in range(R):
        if board[i][king]:
            s,d,z = board[i][king]
            board[i][king] = False
            ans+=z
            break
    tmp = {}
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                s,d,z = board[i][j]
                board[i][j] = False
                ni = (i+di[d]*s)%(2*(R-1))
                nj = (j+dj[d]*s)%(2*(C-1))
                nd = d
                if ni>R-1 or nj>C-1:
                    nd = next_d[d]
                    if ni>R-1:
                        ni = 2*(R-1)-ni
                    else:
                        nj = 2*(C-1)-nj
                if (ni,nj) in tmp:
                    ss,dd,zz = tmp[(ni,nj)]
                    if z>zz:
                        tmp[(ni,nj)]=(s,nd,z)
                else:
                    tmp[(ni,nj)]=(s,nd,z)
    for i,j in tmp:
        board[i][j] = tmp[(i,j)]
print(ans)