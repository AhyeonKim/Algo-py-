N = int(input())
M = int(input())
budgets = [list(map(int,input().split())) for _ in range(M)]
budgets.sort(key=lambda x:x[2])
parents = [i for i in range(N)] # 부모 노드
answer=0
def find(a):
    if parents[a]==a:
        return a
    parents[a] = find(parents[a])
    return parents[a]
def union(a,b):
    p1 = find(a)
    p2 = find(b)
    if p1!=p2:
        parents[p1]=p2
    return
for i in range(len(budgets)):
    a,b,c = budgets[i]
    a-=1
    b-=1
    if find(a)!=find(b):
        union(a,b)
        answer+=c
print(answer)
