n = int(input())

num_list = list(map(int, input().split()))
dp = [1] * n
k = 0
for i in num_list:
    dp[k] = i
    k += 1

for i in range(1, n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[j]+num_list[i], dp[i])
print(max(dp))