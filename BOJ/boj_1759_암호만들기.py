def make(s,idx,v,c):
    if len(s)==L:
        if v>0 and c>1:
            print(''.join(s))
            return
    if idx==C:
        return
    is_v = 0
    is_c = 0
    if arr[idx] in ['a','e','i','o','u']:
        is_v = 1
    else:
        is_c = 1
    make(s+[arr[idx]],idx+1,v+is_v,c+is_c)
    make(s,idx+1,v,c)
L,C = map(int,input().split())
arr = list(input().split())
arr.sort()
make([],0,0,0)