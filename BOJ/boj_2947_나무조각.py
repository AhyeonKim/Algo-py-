arr = list(map(int,input().split()))
while True:
    for i in range(len(arr)-1):
        j = i+1
        if arr[i]>arr[j]:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
            print(*arr)
    if arr==[1,2,3,4,5]:
        break

