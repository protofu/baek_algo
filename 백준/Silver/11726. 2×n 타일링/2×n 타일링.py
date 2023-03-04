import sys
input = sys.stdin.readline

num = int(input())

dp = [0, 1, 2]
for n in range(3, num+1):
    dp.append(dp[n-2] + dp[n-1])
print(dp[num]%10007)