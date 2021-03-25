import sys
input = sys.stdin.readline
di, dj = [-1,1,0,0], [0,0,-1,1]
N,M,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
shark = list(map(int,input().split()))
priority = {}
for i in range(M):
    priority[i] = []
    for _ in range(4):
        priority[i].append(list(map(int,input().split())))
print(priority)