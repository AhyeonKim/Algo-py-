import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    i = input().strip().split()
    length = len(stack)
    if i[0]=="push":
        stack.append(i[1])
    elif i[0]=="pop":
        if length>0:
            print(stack.pop())
        else:
            print(-1)
    elif i[0]=="size":
        print(length)
    elif i[0]=="empty":
        print(1 if length==0 else 0)
    elif i[0]=="top":
        if length>0:
            print(stack[length-1])
        else:
            print(-1)