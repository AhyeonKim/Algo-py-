di, dj = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
N,M,K = map(int,input().split())
balls = []
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    balls.append((r,c,m,s,d))
move = 0
while move<K:
    move+=1
    tmp = {}
    for ball in balls:
        r,c,m,s,d = ball
        nr,nc = (r+di[d]*s)%N, (c+dj[d]*s)%N
        if (nr,nc) in tmp:
            tmp[(nr,nc)].append((m,s,d))
        else:
            tmp[(nr,nc)]=[(m,s,d)]
    balls=[]
    for r,c in tmp:
        if len(tmp[(r,c)])>1:
            length = len(tmp[(r,c)])
            m_sum=0
            s_sum=0
            d_sum=0
            for t in tmp[(r,c)]:
                m,s,d = t
                m_sum+=m
                s_sum+=s
                d_sum+=d%2
            new_m = m_sum//5
            if new_m>0:
                new_s = s_sum//length
                new_d = []
                if d_sum==0 or d_sum==length:
                    new_d = [0,2,4,6]
                else:
                    new_d = [1,3,5,7]
                for d in new_d:
                    balls.append((r,c,new_m,new_s,d))
        else:
            m,s,d = tmp[(r,c)][0]
            balls.append((r,c,m,s,d))
answer = 0
for ball in balls:
    r,c,m,s,d = ball
    answer+=m
print(answer)