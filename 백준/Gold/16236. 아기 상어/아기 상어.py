from collections import deque

N = int(input())
box = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
y = x = 0
for i in range(N):
    for j in range(N):
        if box[i][j] == 9:
            y, x = i, j


def bfs(y, x):
    visited = [[0] * N for _ in range(N)]
    Q = deque([[y, x]])
    visited[y][x] = 1
    lst = []
    while Q:
        ay, ax = Q.popleft()
        for i in range(4):
            ny, nx = ay + dy[i], ax + dx[i]
            if N > ny >= 0 and N > nx >= 0 and not visited[ny][nx]:
                if box[y][x] > box[ny][nx] and box[ny][nx]:
                    visited[ny][nx] = visited[ay][ax] + 1
                    lst.append([visited[ny][nx] -1, ny, nx])
                elif box[y][x] == box[ny][nx]:
                    visited[ny][nx] = visited[ay][ax] + 1
                    Q.append([ny, nx])
                elif not box[ny][nx]:
                    visited[ny][nx] = visited[ay][ax] + 1
                    Q.append([ny, nx])

    return sorted(lst, key = lambda i: [i[0], i[1], i[2]])
posi = [2, 0]
ans = 0
while True:
    box[y][x] = posi[0]
    lst = deque(bfs(y, x))

    if not lst:
        break

    cnt, cy, cx = lst.popleft()
    ans += cnt
    posi[1] += 1

    if posi[0] == posi[1]:
        posi[0] += 1
        posi[1] = 0
    box[y][x] = 0
    y, x = cy, cx
print(ans)

