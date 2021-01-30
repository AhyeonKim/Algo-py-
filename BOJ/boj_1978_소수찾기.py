N = int(input())
arr = list(map(int,input().split()))
cnt = 0
for n in arr:
    if n==1:
        continue
    for i in range(2,n):
        if n%i==0:
            break
    else:
        cnt+=1
print(cnt)