from bisect import bisect_left

N = int(input())
num_list = list(map(int, input().split()))
dp = [0]

for i in num_list:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[bisect_left(dp, i)] = i

print(len(dp)-1)
