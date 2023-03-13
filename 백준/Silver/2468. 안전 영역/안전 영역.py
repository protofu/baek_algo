from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
ans = 1
for i in ground:
    if max(i) > max_num:
        max_num = max(i)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x, h):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if N > ny >= 0 and N > nx >= 0 and not visited[ny][nx]:
            if ground[ny][nx] > h:
                visited[ny][nx] = 1
                dfs(ny, nx, h)

for h in range(max_num):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if ground[y][x] > h and not visited[y][x]:
                cnt += 1
                visited[y][x] = 1
                dfs(y, x, h)
    ans = max(ans, cnt)
print(ans)