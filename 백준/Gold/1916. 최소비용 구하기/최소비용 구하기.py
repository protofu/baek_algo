INF = 100000001
n = int(input())
m = int(input())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
d = [INF for _ in range(n+1)]
visit = [False for _ in range(n+1)]


def minIndex():
    minValue = INF
    idx = 0
    for i in range(1, n+1):
        if not visit[i] and minValue > d[i]:
            minValue = d[i]
            idx = i
    return idx


def dijkstra(x):
    for i in range(1, n+1):
        d[i] = graph[x][i]
    visit[x] = True

    for _ in range(n-2):
        x = minIndex()
        visit[x] = True
        for i in range(1, n+1):
            if not visit[i] and graph[x][i] + d[x] < d[i]:
                d[i] = graph[x][i] + d[x]
    print(d[e])


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

s, e = map(int, input().split())

dijkstra(s)