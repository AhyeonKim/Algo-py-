tc = int(input())
for _ in range(tc):
    N, M = map(int,input().split())
    p = []
    tmp = list(map(int,input().split()))
    for i in range(len(tmp)):
        p.append([tmp[i],i])
    turn = 0
    while True:
        flag = False
        for i in range(1,len(p)):
            priority = p[0][0]
            if p[i][0]>priority:
                p.append(p.pop(0))
                flag = True
                break
        if not flag:
            turn+=1
            if p[0][1]==M:
                break
            else:
                p.pop(0)
    print(turn)