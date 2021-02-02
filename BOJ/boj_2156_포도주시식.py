import sys
input = sys.stdin.readline
n = int(input())
step = []
for _ in range(n):
    step.append(int(input()))
dp = [step[0]]
for i in range(1,n):
    one = dp[i-2]+step[i]
    two = step[i-1]+step[i]
    if i-3>-1:
        two+=dp[i-3]
    dp.append(max(one,two,dp[i-1]))
print(max(dp))