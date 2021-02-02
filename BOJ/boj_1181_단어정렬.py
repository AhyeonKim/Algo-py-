import sys
input = sys.stdin.readline
N = int(input())
s = set()
for _ in range(N):
    s.add(input().strip())
s=sorted(s,key=lambda x:[len(x),x])
for i in s:
    print(i)