import sys
input = sys.stdin.readline
N = int(input())
people = []
for _ in range(N):
    a, b = input().split()
    people.append([int(a),b])
people = sorted(people,key=lambda x:x[0])
for p in people:
    print(*p)