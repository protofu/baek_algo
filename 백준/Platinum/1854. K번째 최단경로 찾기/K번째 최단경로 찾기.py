import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    Q = [[0, start]]
    dist[start][0] = 0
    while Q:
        cost, start = heapq.heappop(Q)
        for n, distance in graph[start]:
            real_cost = cost + distance
            if dist[n][K-1] > real_cost:
                dist[n][K-1] = real_cost
                dist[n].sort()
                heapq.heappush(Q, [real_cost, n])



INF = int(1e9)
N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
start = 1
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
dist = [[INF]*K for _ in range(N + 1)]
dijkstra(start)
for i in range(1, N+1):
    if dist[i][K - 1] != INF:
        print(dist[i][K - 1])
    else:
        print(-1)