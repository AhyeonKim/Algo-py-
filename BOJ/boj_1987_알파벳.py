di,dj = [0,-1,0,1],[-1,0,1,0]
R,C = map(int,input().split())
arr = []
for _ in range(R):
    arr.append(input())
queue = set([(0,0,1,arr[0][0])])
ans = 0
while queue:
    i,j,cnt,history=queue.pop()
    ans = max(ans,cnt)
    for d in range(4):
        ni,nj = i+di[d], j+dj[d]
        if -1<ni<R and -1<nj<C and arr[ni][nj] not in history:
            queue.add((ni,nj,cnt+1,history+arr[ni][nj]))
print(ans)