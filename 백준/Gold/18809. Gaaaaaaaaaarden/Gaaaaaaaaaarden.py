'''
0은 호수, 1은 배양액 안되는 땅, 2는 배양액 가능 땅
배양액 가능 땅은 R+G 이상 10개 이하
도달한 시간이 동일할 때 꽃이 핀다.

배양액은 하나씩 뿌릴 수 있는데...
'''
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(gl, rl, sandbox):
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    cnt = 0
    for g in gl:
        Q.append((g[0], g[1], 'g'))
        visited[g[0]][g[1]] = -1
    for r in rl:
        Q.append((r[0], r[1], 'r'))
        visited[r[0]][r[1]] = 1

    while Q:
        y, x, c = Q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and sandbox[ny][nx] and visited[ny][nx]==0:
                if visited[y][x] < 0:
                    visited[ny][nx] = visited[y][x] - 1
                    Q.append((ny, nx, c))
                elif 1e6>visited[y][x] > 0:
                    visited[ny][nx] = visited[y][x] + 1
                    Q.append((ny, nx, c))
            if 0 <= ny < N and 0 <= nx < M and sandbox[ny][nx] and not(visited[ny][nx] + visited[y][x] + 1):
                visited[ny][nx] = 1e6
                cnt += 1
    return cnt

N, M, G, R = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
canGrow = []

for y in range(N):
    for x in range(M):
        if ground[y][x] == 2:
           canGrow.append((y, x))

sand = set(canGrow)
ans = 0
for green in combinations(canGrow, G):
    notGreenGround = list(sand-set(green))
    greenList = list(green)
    for red in combinations(notGreenGround, R):
        redList = list(red)
        tmp = bfs(greenList, redList, ground)
        if ans < tmp:
            ans = tmp
print(ans)