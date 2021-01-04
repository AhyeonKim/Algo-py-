from itertools import permutations

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

op = []

for i in range(4):
    op += [i] * B[i]

max_r = -(10**10)
min_r = 10**10
for p in permutations(op):
    tmp = list(p)
    k = 0
    result = A[0]
    for i in range (1,len(A)):
        if tmp[k]==0:
            result += A[i]
        elif tmp[k]==1:
            result -= A[i]
        elif tmp[k]==2:
            result *= A[i]
        elif tmp[k]==3:
            if result<0:
                result = -result//A[i]*-1
            else:
                result //= A[i]
        k+=1

    max_r = max(result,max_r)
    min_r = min(result,min_r)

print(max_r)
print(min_r)
