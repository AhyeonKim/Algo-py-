A = int(input())
B = int(input())
C = int(input())

num = [0]*10
result = str(A*B*C)
for i in result:
    num[int(i)]+=1
for i in num:
    print(i)