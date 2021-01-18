from collections import deque
import sys
input = sys.stdin.readline
T = int(input().strip())

def q():
    if len(tmp)>2:
        arr = deque(tmp[1:-1].split(','))
    else:
        arr = deque([])
    r = False
    for i in p:
        if i=='R':
            r = not r
        else:
            if arr:
                if r:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                return 'error'
    if r:
        arr.reverse()
    return '['+','.join(arr)+']'

for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    tmp = input().strip()
    print(q())