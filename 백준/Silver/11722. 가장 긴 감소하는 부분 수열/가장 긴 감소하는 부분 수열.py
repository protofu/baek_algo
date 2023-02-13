n = int(input())

num_list = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if num_list[i] < num_list[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))