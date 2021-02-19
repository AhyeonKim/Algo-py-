N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
ans = 0
di,dj = [0,-1,0,1],[-1,0,1,0]
ti = [[0,0,1],[0,-1,1],[-1,0,0],[-1,1,0]]
tj = [[-1,1,0],[-1,0,0],[0,-1,1],[0,0,1]]
for y in range(N):
    for x in range(M):
        q=[(y,x,arr[y][x],1,0)]
        while q:
            for _ in range(len(q)):
                i,j,s,c,prev_d = q.pop()
                if c==4:
                    ans=max(ans,s)
                else:
                    for d in range(4):
                        ni = i+di[d]
                        nj = j+dj[d]
                        if -1<ni<N and -1<nj<M and abs(prev_d-d)!=2:
                            q.append((ni,nj,s+arr[ni][nj],c+1,d))
for t in range(4):
    for i in range(N):
        for j in range(M):
            s=arr[i][j]
            c=1
            for d in range(3):
                ni=i+ti[t][d]
                nj=j+tj[t][d]
                if -1<ni<N and -1<nj<M:
                    s+=arr[ni][nj]
                    c+=1
                else:
                    break
            if c==4:
                ans=max(ans,s)
print(ans)