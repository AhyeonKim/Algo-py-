import sys
input = sys.stdin.readline
N,M,x,y,K = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
move = list(map(int,input().split()))
# ㅋㅋ