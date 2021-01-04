import sys
N, M = map(int,input().split())
cards = list(map(int,input().split()))

diff = sys.maxsize
answer = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            total = cards[i]+cards[j]+cards[k]
            if 0<=M-total<diff:
                diff = M-total
                answer = total

print(answer)

answer = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            total = cards[i]+cards[j]+cards[k]
            if answer < total <= M :
                answer = total
print(answer)