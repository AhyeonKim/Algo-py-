def check(line):
    global ans
    cur = line[0]
    visit = [False for _ in range(N)]
    i = 0
    while(i<N):
        if cur==line[i]:
            i+=1
            continue
        else:
            if abs(cur-line[i])!=1:
                return
            else:
                if cur-line[i]==1: #낮아질 때
                    for j in range(L):
                        ni = i+j
                        if ni<N and cur-line[ni]==1 and not visit[ni]:
                            visit[ni] = True
                        else:
                            return
                    cur=line[i]
                    i+=L
                elif cur-line[i]==-1: #높아질 때
                    for j in range(1,L+1):
                        ni = i-j
                        if -1<ni and cur==line[ni] and not visit[ni]:
                            visit[ni] = True
                        else:
                            return
                    cur=line[i]
                    i+=1
    ans+=1
    return
N,L = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in board:
    check(i)
for j in range(N):
    tmp = []
    for i in range(N):
        tmp.append(board[i][j])
    check(tmp)
print(ans)