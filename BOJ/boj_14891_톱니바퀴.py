def turn(gear,dir):
    if(dir==-1):
        tmp = gear.pop(0)
        gear = gear+[tmp]
    else:
        tmp = gear.pop()
        gear = [tmp]+gear
    # print(gear)
    return gear

def start(num,dir):
    # print('spin',num)
    gears[num] = turn(gears[num],dir)
    visit[num] = True
    if 0<num and not visit[num-1]:
        if gears[num][6+dir]!=gears[num-1][2]:
            start(num-1,dir*-1)
    
    if num<3 and not visit[num+1]:
        if gears[num][2+dir]!=gears[num+1][6]:
            start(num+1,dir*-1)

gears = []
# input().split() - > ['1','2','3']
# '11010111' -> '11010111'
for _ in range(4):
    gears.append(list(map(int,input())))
K = int(input())
for _ in range(K):
    s, d = list(map(int,input().split()))
    visit = [False]*4
    start(s-1,d)

answer = 0
for i in range(4):
    if gears[i][0]:
        answer += 2**i
print(answer)
