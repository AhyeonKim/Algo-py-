N = int(input())
ans=0
if N//100<1:
    ans=N
else:
    ans+=99
    for i in range(111,N+1):
        n1 = i//100
        i = i%100
        n2 = i//10
        n3 = i%10
        if n1-n2==n2-n3:
            ans+=1
print(ans)