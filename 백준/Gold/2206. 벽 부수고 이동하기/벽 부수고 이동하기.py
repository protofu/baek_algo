import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
rlt = []

def bfs():
    Q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while Q:
        y, x, wall = Q.popleft()
        if y == N-1 and x == M-1:
            return visited[y][x][wall]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if N > ny >= 0 and M > nx >= 0 and not visited[ny][nx][wall]:
                if not box[ny][nx]:
                    Q.append((ny, nx, wall))
                    visited[ny][nx][wall] = visited[y][x][wall] + 1
                if box[ny][nx] and not wall:
                    Q.append((ny, nx, 1))
                    visited[ny][nx][1] = visited[y][x][wall] + 1
    return -1
print(bfs())
