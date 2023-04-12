N = int(input())
INF = 1e9
graph = [[INF]*N for _ in range(N)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                graph[i][j] = 0
            if graph[i][j] == 1 or graph[i][j] == 0:
                continue
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

ans = 0
rlt = []
for i in range(N):
    rlt.append(max(graph[i]))

ans = min(rlt)
print(ans, rlt.count(ans))
for i in range(N):
    if rlt[i] == ans:
        print(i+1, end=' ')


