def step2(new_id):
    tmp=''
    for i in new_id:
        if ord('a')<=ord(i)<=ord('z') or ord('0')<=ord(i)<=ord('9') or i in ['-','_','.']:
            tmp+=i
    return tmp
def step3(new_id):
    tmp=''
    for i in new_id:
        if i=='.':
            if len(tmp)==0:
                tmp+=i
            elif tmp[-1]!='.':
                tmp+=i
        else:
            tmp+=i
    return tmp
def step4(new_id):
    tmp=''
    if new_id and new_id[0]=='.':
        tmp = new_id[1:]
    else:
        tmp = new_id
    if tmp and tmp[-1]=='.':
        tmp = tmp[:-1]
    return tmp
def solution(new_id):
    new_id = new_id.lower()
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id='a' if len(new_id)==0 else new_id[:15]
    if new_id[-1]=='.':
        new_id = new_id[:-1]
    while len(new_id)<3:
        new_id+=new_id[-1]
    return new_id