T = int(input())
for _ in range(T):
    N = int(input())
    P = [1,1,1,2,2,3,4,5,7,9]
    for i in range(10,N):
        P.append(P[i-3]+P[i-2])
    print(P[N-1])