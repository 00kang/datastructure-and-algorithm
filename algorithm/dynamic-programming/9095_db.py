# 백준 | [400]다이나믹 프로그래밍 1 | #9095 | 1,2,3 더하기 | 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

t = int(input())

dp = [0,1,2,4]
for i in range(4, 12):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in range(t):
    n = int(input())
    print(dp[n])