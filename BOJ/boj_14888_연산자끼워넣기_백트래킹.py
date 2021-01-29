def select(x,n):
    global max_r, min_r
    if n==N:
        max_r = max(max_r,x)
        min_r = min(min_r,x)
        return
    for i in range(len(op)):
        if op[i]!=0:
            op[i]-=1
            if i==0:
                select(x+A[n],n+1)
            elif i==1:
                select(x-A[n],n+1)
            elif i==2:
                select(x*A[n],n+1)
            else:
                if x<0:
                    select((-x//A[n])*-1,n+1)
                else:
                    select(x//A[n],n+1)
            op[i]+=1
            
N = int(input())
A = list(map(int,input().split()))
op = list(map(int,input().split()))
max_r, min_r = -(10**10),10**10
select(A[0],1)
print(max_r)
print(min_r)