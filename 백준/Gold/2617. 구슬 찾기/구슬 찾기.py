N, M = map(int, input().split())
INF = 1e9
graph = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):

            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
            if i == j:
                graph[i][j] = 0
ans = 0
for i in range(N):
    left_cnt = 0
    right_cnt = 0
    for j in range(N):
        if i == j:
            continue
        elif graph[i][j] == 1:
            right_cnt += 1
        elif graph[j][i] == 1:
            left_cnt += 1
    if right_cnt > N//2 or left_cnt > N//2:
        ans += 1

print(ans)