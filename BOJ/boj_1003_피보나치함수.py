T = int(input())
fibonacci = []
fibonacci.append([1,0])
fibonacci.append([0,1])
for i in range(2,41):
    fibonacci.append([fibonacci[i-2][0]+fibonacci[i-1][0],fibonacci[i-2][1]+fibonacci[i-1][1]])
for _ in range(T):
    N = int(input())
    print(fibonacci[N][0],fibonacci[N][1])