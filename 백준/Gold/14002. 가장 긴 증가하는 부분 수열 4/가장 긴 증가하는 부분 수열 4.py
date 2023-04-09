N = int(input())
num_list = list(map(int, input().split()))
dp = [1]*N
lst = []

for i in range(1, N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

order = max(dp)
for i in range(N-1, -1, -1):
    if dp[i] == order:
        lst.append(num_list[i])
        order -= 1
lst.reverse()
for i in lst:
    print(i, end=' ')