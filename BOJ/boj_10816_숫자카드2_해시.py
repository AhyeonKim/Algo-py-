N = int(input())
card = list(map(int,input().split()))
M = int(input())
card2 = list(map(int,input().split()))
count = {}
for c in card:
    if c in count:
        count[c]+=1
    else:
        count[c]=1
answer = []
for c2 in card2:
    if c2 in count:
        answer.append(str(count[c2]))
    else:
        answer.append('0')
print(' '.join(answer))