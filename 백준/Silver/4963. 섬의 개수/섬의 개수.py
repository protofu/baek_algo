from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(y, x, mat):
    queue = deque()
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= nx < w and 0 <= ny < h and mat[ny][nx]:
                queue.append([ny, nx])
                mat[ny][nx] = 0

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    mat = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    for y in range(h):
        for x in range(w):
            if mat[y][x]:
                mat[y][x] = 0
                bfs(y, x, mat)
                ans += 1
    print(ans)