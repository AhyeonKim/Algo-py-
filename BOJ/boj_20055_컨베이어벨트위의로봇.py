N,K = map(int,input().split())
belt = list(map(int,input().split()))
robot = [False]*N
step=0
cnt=0
while True:
    step+=1
    tmp = belt[len(belt)-1]
    belt = [tmp]+belt[:-1]
    robot = [False]+robot[:-1]
    robot[N-1]=False
    for i in range(N-2,-1,-1):
        if robot[i] and belt[i+1]>0 and not robot[i+1]:
            robot[i+1]=True
            robot[i]=False
            belt[i+1]-=1
            if belt[i+1]==0:
                cnt+=1
    if belt[0]>0 and not robot[0]:
        robot[0]=True
        belt[0]-=1
        if belt[0]==0:
            cnt+=1
    if cnt>=K:
        break
print(step)