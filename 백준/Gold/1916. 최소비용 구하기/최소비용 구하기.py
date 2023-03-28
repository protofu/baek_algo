import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
dist = [INF for _ in range(N + 1)]


for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

start, end = map(int, input().split())

def dijkstra(start):
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
dijkstra(start)
print(dist[end])