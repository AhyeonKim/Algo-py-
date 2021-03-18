def solution(clothes):
    answer = 0
    cloth = {}
    for c in clothes:
        k = c[1]
        if k in cloth:
            cloth[k].append(c[0])
        else:
            cloth[k]=[c[0]]
    cnt = 1
    for c in cloth:
        cnt*=(len(cloth[c])+1)
    answer = answer+cnt-1
    return answer