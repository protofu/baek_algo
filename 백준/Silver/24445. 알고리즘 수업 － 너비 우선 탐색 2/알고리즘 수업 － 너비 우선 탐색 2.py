from collections import deque

def bfs():
    cnt = 1
    visited[R] = cnt
    Q = deque()
    Q.append(R)
    while Q:
        k = Q.popleft()
        graph[k].sort(reverse=True)
        for s in graph[k]:
            if not visited[s]:
                cnt += 1
                visited[s] = cnt
                Q.append(s)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()
for i in visited[1:]:
    print(i)