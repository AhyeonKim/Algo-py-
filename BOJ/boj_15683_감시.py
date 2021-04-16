import sys
input = sys.stdin.readline
def isIn(i,j):
    return -1<i<N and -1<j<N
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer = 0
print(board)