N = int(input())
M = int(input())
INF = 1e9
graph = [[INF]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = 1
ans = 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if graph[i][j] == 1:
            cnt += 1
        if graph[j][i] == 1:
            cnt += 1
    print(N-1-cnt)

