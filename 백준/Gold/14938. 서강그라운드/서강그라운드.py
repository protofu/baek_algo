INF = int(1e9)

N, M, R = map(int, input().split())
item = list(map(int, input().split()))
visited = [[INF] * N for _ in range(N)]
MAX = 0

for _ in range(R):
    s, e, d = map(int, input().split())
    visited[s-1][e-1] = min(visited[s-1][e-1], d)
    visited[e-1][s-1] = min(visited[e-1][s-1], d)

for i in range(N):
    for j in range(N):
        for k in range(N):
            visited[j][k] = min(visited[j][k], visited[j][i] + visited[i][k])
            if j == k:
                visited[j][k] = False

for i in range(N):
    cnt = 0
    for j in range(N):
        if visited[i][j] <= M:
            cnt += item[j]
    MAX = max(MAX, cnt)
print(MAX)