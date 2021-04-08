import sys
sys.setrecursionlimit(10 **6)

def isIn(i,j):
    return 0<=i<N and 0<=j<N

N, L, R = map(int,input().split())
ground=[]
for _ in range(N):
    ground.append(list(map(int,input().split())))