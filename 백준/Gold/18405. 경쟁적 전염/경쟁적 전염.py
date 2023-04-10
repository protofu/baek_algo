from collections import deque

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs():
    Q = deque(virus)
    cnt = 0
    while Q:
        if cnt == S:
            break
        for _ in range(len(Q)):
            c, y, x = Q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not graph[ny][nx]:
                    graph[ny][nx] = c
                    Q.append([graph[ny][nx], ny, nx])
        cnt += 1
    return graph[a-1][b-1]

N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j]:
            virus.append([graph[i][j], i, j])

S, a, b = map(int, input().split())
virus.sort()
print(bfs())

