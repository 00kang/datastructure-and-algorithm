# 백준 | [400]다이나믹 프로그래밍 1 | #11052 | 카드 구매하기 | 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

n = int(input())
card = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], card[j] + dp[i-j])

print(dp[n])