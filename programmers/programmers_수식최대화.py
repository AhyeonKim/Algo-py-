rules = ['*+-','*-+','+*-','+-*','-+*','-*+']
def calc(nums,operators,rule,i):
    if i==3:
        return nums[0]
    else:
        idx = 0
        new_nums = [nums[idx]]
        new_operators = []
        for op in operators:
            idx+=1
            next_num = nums[idx]
            if op==rule[i]:
                if op=='*':
                    new_nums[-1]*=next_num
                if op=='+':
                    new_nums[-1]+=next_num
                if op=='-':
                    new_nums[-1]-=next_num
            else:
                new_nums.append(next_num)
                new_operators.append(op)
        return calc(new_nums,new_operators,rule,i+1)
def solution(expression):
    answer = 0
    tmp=''
    nums=[]
    operators=[]
    for e in expression:
        if '0'<=e<='9':
            tmp+=e
        else:
            nums.append(int(tmp))
            operators.append(e)
            tmp=''
    nums.append(int(tmp))
    for rule in rules:
        result = calc(nums,operators,rule,0)
        answer = max(answer,abs(result))
    return answer