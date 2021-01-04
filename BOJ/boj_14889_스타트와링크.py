from itertools import combinations
import sys

N = int(input())

power = []
for _ in range(N):
    power.append(list(map(int,input().split())))

a = []
for i in range(1,N+1):
    a.append(i)

ans = sys.maxsize

combi = combinations(a,N//2)

for c in combi:
    start = list(c)
    link = list(set(a)-set(start))
    
    s_p = 0
    l_p = 0
    for x in start:
        for y in start:
            s_p += power[x-1][y-1]
    for x in link:
        for y in link:
            l_p += power[x-1][y-1]

    diff = abs(s_p-l_p)
    if(diff<ans):
        ans = diff

print(ans)