def solution(citations):
    answer = 0
    info = []
    citations.sort(reverse=True)
    cur = citations[0]
    cnt = 1
    for i in range(1,len(citations)):
        if cur!=citations[i]:
            info.append((cur,cnt))
            cur = citations[i]
            cnt = 1
        else:
            cnt+=1
    info.append((cur,cnt))
    h = info[0][0]
    while True:
        a,b=0,0
        for i in range(0,len(info)):
            if info[i][0]>=h:
                a+=info[i][1]
            else:
                b+=info[i][1]
        if a>=h and b<=h:
            answer = h
            break
        h-=1
    return answer