import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = sys.maxsize
V, E = map(int, input().split())

S = int(input())
node = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V+1)]

def dijk(s):
    node[s] = 0
    heapq.heappush(heap,(0,s))
    while heap:
        w, n = heapq.heappop(heap)
        if node[n] < w:
            continue
        for wei, n_node in graph[n]:
            n_w = w + wei
            if n_w < node[n_node]:
                node[n_node] = n_w
                heapq.heappush(heap, (n_w, n_node))
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
dijk(S)
for i in range(1, V+1):
    print("INF" if node[i] == INF else node[i])