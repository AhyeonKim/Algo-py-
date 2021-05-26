def solution(answers):
    ans = [0]*3
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    l1,l2,l3 = len(s1),len(s2),len(s3)
    for idx, a in enumerate(answers):
        if a==s1[idx%l1]:
            ans[0]+=1
        if a==s2[idx%l2]:
            ans[1]+=1
        if a==s3[idx%l3]:
            ans[2]+=1
    max_ans = max(ans)
    answer=[]
    for idx,a in enumerate(ans):
        if a==max_ans:
            answer.append(idx+1)
    return answer