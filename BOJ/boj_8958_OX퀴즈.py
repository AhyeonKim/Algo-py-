N = int(input())
for _ in range(N):
    ans = 0
    cur = 0
    result = input()
    for i in result:
        if i=='O':
            cur+=1
            ans+=cur
        else:
            cur=0
    print(ans)