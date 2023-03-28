def get_smallest_node():
    min_value = INF
    idx = 1
    for i in range(1, N+1):
        if dist[i] < min_value and not visited[i]:
            min_value = dist[i]
            idx = i
    return idx

def dijkstra(start):
    dist[start] = 0
    visited[start] = True

    for j in graph[start]:
        if dist[j[0]] > j[1]:
            dist[j[0]] = j[1]

    for _ in range(N-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = dist[now] + j[1]
            if cost < dist[j[0]] and not visited[j[0]]:
                dist[j[0]] = cost

INF = int(1e9)
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
dist = [INF for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())

dijkstra(start)
if end == start:
    print(0)
else:
    print(dist[end])
