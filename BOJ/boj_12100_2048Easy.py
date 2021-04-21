def go(bo,cnt):
    global answer
    if cnt==5:
        max_value = max(map(max,bo))
        answer=max(answer,max_value)
        return
    for d in range(4):
        nb = pull(d,bo)
        go(nb,cnt+1)

def pull(dr,boa):
    copy = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            copy[y][x] = boa[y][x]
    if dr==0 or dr==1:
        for i in range(len(copy)):
            l = copy[i]
            if dr==1:
                l.reverse()
            result = sum_line(l)
            if dr==1:
                result.reverse()
            copy[i] = result
    else:
        for j in range(N):
            l = []
            for i in range(N):
                l.append(copy[i][j])
            if dr==3:
                l.reverse()
            result = sum_line(l)
            if dr==3:
                result.reverse()
            for ii in range(N):
                copy[ii][j] = result[ii]
    return copy

def sum_line(line):
    prev = 0
    tmp = []
    for i in line:
      if i:
        if prev == i:
          tmp.append(prev*2)
          prev = 0
        else:
          if prev:
            tmp.append(prev)
          prev = i
    if prev:
      tmp.append(prev)
    return tmp + [0]*(len(line)-len(tmp))

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
answer = 0
go(board,0)
print(answer)