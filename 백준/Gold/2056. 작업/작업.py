N = int(input())
dp = [0]*N
for i in range(N):
    time, num, *lst = map(int, input().split())
    dp[i] = time
    for j in lst:
        dp[i] = max(dp[i], time+dp[j-1])
print(max(dp))