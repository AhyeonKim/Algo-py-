n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
for i in range(len(arr)):
    if i==0:
        continue
    for j in range(len(arr[i])):
        left,right = 0,0
        if j-1>-1:
            left = arr[i-1][j-1]
        if j<len(arr[i-1]):
            right = arr[i-1][j]
        arr[i][j]+=max(left,right)
print(max(arr[n-1]))