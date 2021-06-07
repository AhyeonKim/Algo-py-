from heapq import heappush,heappop
import sys
input = sys.stdin.readline
def pop(hq):
    global check
    while hq:
        num,idx = heappop(hq)
        if not check[idx]:
            check[idx]=True
            return num
for _ in range(int(input())):
    k = int(input())
    min_q,max_q = [],[]
    check = [False] * k
    cnt = 0
    for i in range(k):
        ch, n = input().split()
        n = int(n)
        if ch=='I':
            heappush(min_q,(n,i))
            heappush(max_q,(-n,i))
            cnt+=1
        else:
            if n>0:
                pop(max_q)
            else:
                pop(min_q)
    if sum(check) == cnt:
        print('EMPTY')
    elif sum(check) == cnt-1:
        a = pop(min_q)
        print(a,a)
    else:
        print(-pop(max_q),pop(min_q))