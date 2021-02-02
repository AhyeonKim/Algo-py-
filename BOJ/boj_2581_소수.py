M =int(input())
N =int(input())
prime = [True]*(N+1)
prime[0] = False
prime[1] = False
for i in range(2,N+1):
    if prime[i]:
        for j in range(i*2,N+1,i):
            if j%i==0:
                prime[j]=False
min_num=-1
cnt=0
for i in range(M,N+1):
    if prime[i]:
        cnt+=i
        if min_num==-1:
            min_num=i
if min_num!=-1:
    print(cnt)
print(min_num)