N, K = map(int,input().split())
A = []
for _ in range(N):
    A.append(int(input()))
cnt = 0
for i in range(N-1,-1,-1):
    if K<A[i]:
        continue
    elif K>A[i]:
        cnt += K//A[i]
        K = K%A[i]
    else:
        cnt+=1
        break
print(cnt)
