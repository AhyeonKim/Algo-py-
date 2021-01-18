import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque([])
for _ in range(N):
    i = input().strip().split()
    if i[0]=="push_front":
        queue.appendleft(i[1])
    elif i[0]=="push_back":
        queue.append(i[1])
    elif i[0]=="pop_front":
        print(queue.popleft() if queue else -1)
    elif i[0]=="pop_back":
        print(queue.pop() if queue else -1)
    elif i[0]=="size":
        print(len(queue))
    elif i[0]=="empty":
        print(1 if not queue else 0)
    elif i[0]=="front":
        print(queue[0] if queue else -1)
    elif i[0]=="back":
        print(queue[len(queue)-1] if queue else -1)