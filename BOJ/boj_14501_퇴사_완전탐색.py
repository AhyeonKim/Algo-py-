import sys
sys.setrecursionlimit(10**6)
def back(tmp,n):
    global pay
    p = 0
    for i in range(len(tmp)):
        if tmp[i]:
            p += arr[i][1]
        pay = max(pay,p)
    for i in range(n,len(tmp)):
        if not tmp[i] and i+arr[i][0]<=N:
            tmp[i] = True
            back(tmp,i+arr[i][0])
            tmp[i] = False
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
pay = 0
tmp = [False]*N
back(tmp,0)
print(pay)