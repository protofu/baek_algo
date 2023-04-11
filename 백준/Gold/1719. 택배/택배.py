INF = 1e9

def FW():
    for k in range(V):
        for i in range(V):
            for j in range(V):

                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    way[i][j] = way[i][k]
                if i == j:
                    graph[i][j] = 0

    for i in range(V):
        for j in range(V):
            if i == j:
                way[i][j] = '-'

V, E = map(int, input().split())
graph = [[INF]*V for _ in range(V)]
way = [[i for i in range(1, V+1)] for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
    graph[b-1][a-1] = min(graph[b-1][a-1], c)

FW()
ans = INF
for i in way:
    print(*i)
