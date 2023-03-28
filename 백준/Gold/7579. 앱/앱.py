import sys
input = sys.stdin.readline

N, M = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))
a = sum(cost)
table = [[0]*(a+1) for _ in range(N+1)]
ans = INF = int(1e9)

for y in range(N):
    for x in range(a+1):
        if x < cost[y]:
            table[y][x] = table[y-1][x]
        else:
            table[y][x] = max(table[y-1][x], table[y-1][x-cost[y]] + byte[y])
        if table[y][x] >= M:
            ans = min(ans, x)
if not M:
    print(0)
elif N == 1:
    print(cost[0])
elif ans == INF:
    print(N*M)
else:
    print(ans)