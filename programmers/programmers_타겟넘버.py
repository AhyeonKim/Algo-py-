answer = 0
def solution(numbers, target):
    def calcul(idx, total):
        global answer
        if idx==len(numbers):
            if total==target:
                answer+=1
            return
        calcul(idx+1,total+numbers[idx])
        calcul(idx+1,total-numbers[idx])
    calcul(0,0)
    return answer