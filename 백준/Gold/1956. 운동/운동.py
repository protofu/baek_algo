INF = 1e9

V, E = map(int, input().split())
graph = [[INF]*V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for k in range(V):
    for i in range(V):
        for j in range(V):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            if i == j:
                graph[i][j] = 0

ans = INF
for i in range(V):
    for j in range(i, V):
        if i == j:
            continue
        ans = min(ans, graph[i][j]+graph[j][i])
if ans == INF:
    ans = -1
print(ans)