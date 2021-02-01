N = int(input())
people = []
for _ in range(N):
    x,y = map(int,input().split())
    people.append((x,y))
rank = []
for i in people:
    r = 1
    a,b = i
    for j in people:
        if i!=j:
            p,q = j
            if a<p and b<q:
                r+=1
    rank.append(r)
print(*rank)            
