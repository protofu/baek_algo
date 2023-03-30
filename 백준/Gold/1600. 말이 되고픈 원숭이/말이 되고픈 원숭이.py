import sys
from collections import deque
input = sys.stdin.readline

def horse_monkey(r, c, N, cnt):
    Q = deque()
    Q.append((r, c, N, cnt))
    visited[r][c] |= 1 << N
    while Q:
        y, x, N, cnt = Q.popleft()
        if y == H-1 and x == W-1:
            return cnt
        for i in range(12):
            if N <= 0 and i >= 4:
                continue
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and not board[ny][nx]:
                if i >= 4:
                    if not visited[ny][nx] & 1 << (N-1):
                        visited[ny][nx] |= 1 << (N-1)
                        Q.append((ny, nx, N-1, cnt+1))
                else:
                    if not visited[ny][nx] & 1 << (N):
                        visited[ny][nx] |= 1 << (N)
                        Q.append((ny, nx, N, cnt+1))
    return -1


N = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[0]*W for _ in range(H)]
dy, dx = [0, 0, 1, -1, -1, 1, -2, 2, -1, 1, -2, 2], [1, -1, 0, 0, 2, 2, 1, 1,-2, -2, -1, -1]

print(horse_monkey(0, 0, N, 0))
