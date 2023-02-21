def bfs(y, x):
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if N > ny >= 0 and M > nx >= 0 and not visited[ny][nx] and box[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
    print(visited[N - 1][M - 1])


N, M = map(int, input().split())
box = [list(map(int, input())) for _ in range(N)]
queue = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[0] * M for _ in range(N)]
bfs(0,0)
