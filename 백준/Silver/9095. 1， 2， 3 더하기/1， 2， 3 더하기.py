import sys
input = sys.stdin.readline

dp = [0, 1, 2, 4]
for n in range(4, 12):
    dp.append(dp[n-1] + dp[n-2] + dp[n-3])
for _ in range(int(input())):
    print(dp[int(input())])