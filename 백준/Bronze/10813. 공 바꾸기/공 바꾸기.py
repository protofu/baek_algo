import sys

n, m = map(int, sys.stdin.readline().split())

bucket = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    bucket[i], bucket[j] = bucket[j], bucket[i]

print(*bucket)
