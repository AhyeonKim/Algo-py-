def solution(people, limit):
    answer = 0
    s = 0
    p = 0
    people.sort()
    while p!=len(people):
        for i in range(len(people)):
            if people[i]:
                if s:
                    if s+people[i]<=limit:
                        s=0
                        p+=1
                        people[i]=0
                    else:
                        continue
                else:
                    answer+=1
                    s=people[i]
                    p+=1
                    people[i]=0
    return answer