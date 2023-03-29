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
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
rlt = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, N+1):
    rlt.append(dijkstra(X)[i] + dijkstra(i)[X])
print(max(rlt))
