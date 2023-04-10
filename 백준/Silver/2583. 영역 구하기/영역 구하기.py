from collections import deque
import sys
input = sys.stdin.readline

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
def bfs():
    cnt = 1
    Q = deque()
    Q.append([i, j])
    while Q:
        y, x = Q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < M and 0 <= nx < N and not box[ny][nx]:
                Q.append([ny, nx])
                box[ny][nx] = True
                cnt += 1
    return cnt
M, N, K = map(int, input().split())
box = [[False] * (N) for _ in range(M)]
rlt = []
ans = 0
for _ in range(K):
    cx, cy, nx, ny = map(int, input().split())
    for y in range(cy, ny):
        for x in range(cx, nx):
            box[y][x] = True

for i in range(M):
    for j in range(N):
        if not box[i][j]:
            box[i][j] = True
            rlt.append(bfs())
            ans += 1
print(ans)
rlt = sorted(rlt)
print(*rlt)