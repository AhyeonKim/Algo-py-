import sys
input = sys.stdin.readline
def isIn(i,j):
    return -1<i<N and -1<j<N
cctv = {1:[(0,1)],2:[(0,-1),(0,1)],3:[(-1,0),(0,1)],4:[(0,-1),(-1,0),(0,1)],5:[(0,-1),(-1,0),(0,1),(1,0)]}
