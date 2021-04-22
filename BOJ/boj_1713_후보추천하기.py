N = int(input())
M = int(input())    
students = list(map(int,input().split()))
pictures = {}
t = 0
for student in students:
    t+=1
    if student in pictures:
        pictures[student][0]+=1
    else:
        if len(pictures)==N:
            min_s, min_c, min_t = -1,1001,M+1
            for key in pictures:
                snum = pictures[key]
                if snum[0]<min_c:
                    min_s = key
                    min_c = snum[0]
                    min_t = snum[1]
                elif snum[0]==min_c:
                    if snum[1]<min_t:
                        min_s = key
                        min_t = snum[1]
            del pictures[min_s]
        pictures[student] = [1,t]
answer = []
for k in pictures:
    answer.append(k)
answer.sort()
print(*answer)