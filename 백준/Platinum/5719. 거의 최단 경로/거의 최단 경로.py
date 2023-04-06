import sys
from heapq import *
from collections import deque, defaultdict as dfd

input = sys.stdin.readline


def dijkstra():
    pq = []
    heappush(pq, [0, s])
    while pq:
        t, x = heappop(pq)
        for nx in adj[x].keys():
            nt = adj[x][nx]
            if visit[nx] == t + nt: vertex[nx].append(x)
            if visit[nx] > t + nt:
                vertex[nx] = [x]
                visit[nx] = t + nt
                heappush(pq, [t + nt, nx])


while 1:
    n, m = map(int, input().split())
    if n == m == 0: break
    s, d = map(int, input().split())
    adj = [dfd(lambda: 0) for _ in range(n)]
    vertex = [[] for _ in range(n)]
    visit = [float('inf')] * n;
    visit[s] = 0
    for i in range(m):
        u, v, p = map(int, input().split())
        adj[u][v] = p
    dijkstra()
    q = deque([d])
    while q:
        x = q.popleft()
        while vertex[x]:
            nx = vertex[x].pop()
            adj[nx][x] = float('inf')
            q.append(nx)
    visit = [float('inf')] * n;
    visit[s] = 0
    dijkstra()
    print([-1, visit[d]][visit[d] != float('inf')])