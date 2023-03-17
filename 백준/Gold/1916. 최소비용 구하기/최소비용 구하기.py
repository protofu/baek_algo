import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
M = int(input())
inf = 100000000
lst = [[] for i in range(N + 1)]
hq = [inf for i in range(N + 1)]
for i in range(M):
    Q, W, E = map(int, input().split())
    lst[Q].append([W, E])
start, end = map(int, input().split())
def dijkstra(start):
    hq[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        E, N = heappop(heap)
        if hq[N] < E:
            continue
        for n_n, wei in lst[N]:
            n_w = E + wei
            if hq[n_n] > n_w:
                hq[n_n] = n_w
                heappush(heap, [n_w, n_n])
dijkstra(start)
print(hq[end])