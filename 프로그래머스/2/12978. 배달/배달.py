import sys
import heapq as hq

def dij(dist, graph):
    heap = []
    hq.heappush(heap, [1,0])
    while heap:
        node, cost = hq.heappop(heap)
        for n, c in graph[node]:
            if cost+c < dist[n]:
                dist[n] = cost + c
                hq.heappush(heap, [n, cost+c])
            
def solution(N, road, K):
    answer = 0
    # N 마을 수, road 관계, K 목표시간
    dist = [float('inf') for _ in range(N+1)]
    dist[1] = 0
    graph = [[] for _ in range(N+1)]
    for start, end, cost in road:
        graph[start].append([end, cost])
        graph[end].append([start, cost])
    dij(dist, graph)
    answer = len([i for i in dist if i <= K])
    return answer