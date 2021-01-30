arr = [0,1,2,4]
for i in range(4,12):
    arr.append(arr[i-3]+arr[i-2]+arr[i-1])
T = int(input())
for _ in range(T):
    n = int(input())
    print(arr[n])