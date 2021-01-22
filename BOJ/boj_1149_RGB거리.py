N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int,input().split())))
for i in range(1,N):
    for j in range(3):
        compare = []
        for k in range(3):
            if j!=k:
                compare.append(cost[i-1][k])
        cost[i][j]+=min(compare)
print(min(cost[N-1]))