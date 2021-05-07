def solution(lottos, win_nums):
    zeros = 0
    corrects = 0
    rank = [6,6,5,4,3,2,1]
    for i in lottos:
        if not i:
            zeros+=1
        if i in win_nums:
            corrects+=1
    return rank[corrects+zeros],rank[corrects]