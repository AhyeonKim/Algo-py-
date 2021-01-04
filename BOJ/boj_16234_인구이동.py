import sys
sys.setrecursionlimit(10 **6)

def isIn(i,j):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False

def group(i,j):
    global tmp
    visit[i][j] = 1
    tmp.append([i,j])
    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        if isIn(ni,nj) and not visit[ni][nj] and L<=abs(ground[i][j]-ground[ni][nj])<=R:
            group(ni,nj)

N, L, R = map(int,input().split())
ground=[]
for _ in range(N):
    ground.append(list(map(int,input().split())))

day = 0
di , dj = [0,1,0,-1], [1,0,-1,0]

while True:
    union = []
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                tmp = []
                group(i,j)
                union.append(tmp)
    if len(union)==N*N:
        break
    for u in union:
        value = 0
        for i in u:
            value += ground[i[0]][i[1]]
        for i in u:
            ground[i[0]][i[1]] = value//len(u)

    day += 1
print(day)