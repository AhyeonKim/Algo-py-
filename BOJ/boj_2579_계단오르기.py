import sys
input = sys.stdin.readline
N = int(input())
step = []
for _ in range(N):
    step.append(int(input()))
dp = []
dp.append(step[0])
for i in range(1,N):
    one = dp[i-2]+step[i]
    two = step[i-1]+step[i]
    if i-3>-1:
        two += dp[i-3]
    dp.append(max(one,two))
print(dp[-1])