import sys
from  heapq import heappush, heappop
input=sys.stdin.readline

def dijkstra(start):
    dist = [INF for _ in range(N + 1)]
    dist[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        cost, start = heappop(heap)
        if dist[start] < cost:
            continue
        for end_node, distance in graph[start]:
            real_cost = cost + distance
            if dist[end_node] > real_cost:
                dist[end_node] = real_cost
                heappush(heap, [real_cost, end_node])

    return dist
INF = int(1e9)
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


v1_path = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[N]
v2_path = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[N]
ans = min(v1_path, v2_path)
print(ans if ans < INF else -1)

