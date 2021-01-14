import sys
sys.setrecursionlimit(10**6)
def check(i,j):
    for d in range(4):
        ni = i+di[d]
        nj = j+dj[d]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]>r and not visit[ni][nj]:
            visit[ni][nj] = True
            check(ni,nj)

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
max = 1
min = 100
for i in range(N):
    for j in range(N):
        if arr[i][j]<min:
            min = arr[i][j]
        if arr[i][j]>max:
            max = arr[i][j]
di, dj = [0,-1,0,1], [-1,0,1,0]
ans = 1
for r in range(min,max):
    visit = [[False]*(N+1) for _ in range(N+1)]
    count=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]>r and not visit[i][j]:
                count+=1
                visit[i][j] = True
                check(i,j)
    if ans<count:
        ans = count
print(ans)