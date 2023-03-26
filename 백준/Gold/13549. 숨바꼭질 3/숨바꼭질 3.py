import sys, copy
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int,input().split())
INF = 2147000000

def bfs(N,K):
    Q = deque([])
    Q.append((0,N))
    visited = [INF] * (100001)
    visited[N] = 0
    while Q:
        v, n = Q.popleft()
        for i in [(1,n+1), (1,n-1), (0,n*2)]:
            if 0 <= i[1] < 100001:
                if visited[i[1]] > v+i[0]:
                    visited[i[1]] = v+i[0]
                    Q.append((visited[i[1]], i[1]))
    return visited[K]

print(bfs(N,K))