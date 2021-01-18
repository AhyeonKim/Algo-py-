import sys
input = sys.stdin.readline
N = int(input())
queue = []
for _ in range(N):
    i = input().strip().split()
    length = len(queue)
    if i[0]=="push":
        queue.append(i[1])
    elif i[0]=="pop":
        print(queue.pop(0) if length>0 else -1)
    elif i[0]=="size":
        print(length)
    elif i[0]=="empty":
        print(1 if length==0 else 0)
    elif i[0]=="front":
        print(queue[0] if length>0 else -1)
    elif i[0]=="back":
        print(queue[length-1] if length>0 else -1)