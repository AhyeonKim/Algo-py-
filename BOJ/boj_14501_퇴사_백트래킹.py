import sys
sys.setrecursionlimit(10**6)
def back(day,s):
    global mx
    if day == N:
        mx = max(s,mx)
    else:
        if day+T[day] <= N:
            back(day+T[day],s+P[day])
        back(day+1,s)
N = int(input())
T,P = [],[]
for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
mx = 0
back(0,0)
print(mx)