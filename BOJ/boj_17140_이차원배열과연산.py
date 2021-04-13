def sorting(ch,line):
    global R,C
    count = {}
    for x in line:
        if x:
            if x in count:
                count[x]+=1
            else:
                count[x]=1
    info = []
    for k in count:
        info.append([k,count[k]])
    info.sort(key=lambda x:[x[1],x[0]])
    tmp = []
    for x in info:
        tmp.append(x[0])
        tmp.append(x[1])
    if ch=='r':
        C = max(C,len(tmp))
    else:
        R = max(R,len(tmp))
    return tmp
r,c,k = map(int,input().split())
arr = [[0 for _ in range(100)] for _ in range(100)]
i=0
for _ in range(3):
    j=0
    for el in list(map(int,input().split())):
        arr[i][j] = el
        j+=1
    i+=1
t = 0
R = 3
C = 3
while t<=100:
    if arr[r-1][c-1]==k:
        break
    if R>=C:
        for i in range(R):
            tmp = sorting('r',arr[i][:C])[:100]
            arr[i] = tmp + [0] * (100-len(tmp))
    else:
        for j in range(C):
            tmp = []
            for i in range(R):
                tmp.append(arr[i][j])
            result = sorting('c',tmp)[:100]
            for i in range(R):
                if i<len(result):
                    arr[i][j] = result[i]
                else:
                    arr[i][j] = 0
    t+=1       
if t>100:
    print(-1)
else:
    print(t)