import sys
input = sys.stdin.readline
N = int(input())
cnt = [0]*(10001)
for i in range(N):
    cnt[int(input())]+=1
for i in range(len(cnt)):
    for _ in range(cnt[i]):
        print(i)