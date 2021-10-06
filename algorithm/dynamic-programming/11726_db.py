# 백준 | [400]다이나믹 프로그래밍 1 | #11726 | 2xn 타일링 | 다이나믹 프로그래밍

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3,1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)