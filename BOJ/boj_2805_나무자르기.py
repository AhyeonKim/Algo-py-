N,M = map(int,input().split())
trees = list(map(int,input().split()))
left,right = 0,max(trees)
answer = 0
while left<=right:
    mid = (left+right)//2
    m = 0
    for tree in trees:
        if tree-mid>0:
            m+=(tree-mid)
    if m<M:
        right = mid-1
    if m>=M:
        answer = mid
        left = mid+1
print(answer)