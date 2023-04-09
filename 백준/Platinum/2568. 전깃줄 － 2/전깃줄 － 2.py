import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
li = sorted([list(map(int, input().split())) for _ in range(n)])
dp, idx, ans = [], [], []

for l in li:
    cur = bisect_left(dp, l[1])
    if len(dp) != cur:
        dp[cur] = l[1]
    else:
        dp.append(l[1])
    idx.append(cur + 1)

m = len(dp)
print(len(li) - m)
for i in range(len(idx) - 1, -1, -1):
    if idx[i] == m:
        m -= 1
    else:
        ans.append(li[i][0])
for a in ans[::-1]:
    print(a)