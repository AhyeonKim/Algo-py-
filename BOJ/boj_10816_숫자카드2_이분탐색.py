import sys
input = sys.stdin.readline
N = int(input())
card = list(map(int,input().split()))
M = int(input())
card2 = list(map(int,input().split()))
count = {}
card.sort()
for c2 in card2:
    if c2 in count:
        continue
    cnt = 0
    l = 0
    r = len(card)-1
    while l<=r:
        m = (l+r)//2
        if c2<card[m]:
            r = m-1
        elif c2>card[m]:
            l = m+1
        else:
            cnt+=1
            idx = m
            while l<=idx:
                idx-=1
                if idx<0:
                    break
                if card[idx]!=c2:
                    break
                cnt+=1
            idx = m
            while r>=idx:
                idx+=1
                if idx>len(card)-1:
                    break
                if card[idx]!=c2:
                    break
                cnt+=1
            break
    count[c2] = cnt
answer = []
for c2 in card2:
    answer.append(str(count[c2]))
print(' '.join(answer))