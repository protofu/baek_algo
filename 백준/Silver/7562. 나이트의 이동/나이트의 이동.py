import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    r, c = map(int, input().split())
    nr, nc = map(int, input().split())

    board = [[0]*N for _ in range(N)]
    dy, dx = [-1, 1, -2, 2, -1, 1, -2, 2], [2, 2, 1, 1,-2, -2, -1, -1]

    def bfs(r, c, cnt):
        Q = deque()
        Q.append((r, c, cnt))
        while Q:
            y, x, cnt = Q.popleft()
            if y == nr and x == nc:
                return cnt
            for i in range(8):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not board[ny][nx]:
                    board[ny][nx] = 1
                    Q.append((ny, nx, cnt+1))
        return 0
    print(bfs(r, c, 0))
