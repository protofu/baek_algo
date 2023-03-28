import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
table = [0]*(M+1)
for _ in range(N):
    V, C ,K = map(int, input().split())
    cnt = 1
    while K > 0:
        cn = min(cnt, K)
        lst.append((V*cn, C*cn))
        K -= cnt
        cnt *= 2

for wei, val in lst:
    for i in range(M, wei-1, -1):
        table[i] = max(table[i], table[i-wei]+val)

print(table[M])