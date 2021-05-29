def solution(n):
    answer = 0
    prime = [True]*(n+1)
    for i in range(2,n+1):
        k = i
        for j in range(i,n+1,i):
            if k!=j:
                prime[j]=False
    answer = prime.count(True)
    return answer-2