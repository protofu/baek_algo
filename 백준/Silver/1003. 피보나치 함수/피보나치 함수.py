import sys
input = sys.stdin.readline

dp = [[1, 0], [0, 1], [1, 1]]
a = int(input())
for n in range(3, 41):
    dp.append([dp[n-1][1], sum(dp[n-1])])
for _ in range(a):
    print(*dp[int(input())])