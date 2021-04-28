N,M = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()
left,right = trees[0],trees[N-1]
answer = 0
while left<=right:
    mid = left+right//2
    m = 0
    for tree in trees:
        m = m+tree-mid
    if m<M:
        right = mid-1
    if m>=M:
        answer = mid
        left = mid+1
print(answer)