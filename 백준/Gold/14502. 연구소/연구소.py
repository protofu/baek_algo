import sys, copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
ans = 0
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for y in range(N):
        for x in range(M):
            if lab[y][x] == 0:
                lab[y][x] = 1
                wall(cnt+1)
                lab[y][x] = 0

def bfs():
    Q = deque()
    sand_box = copy.deepcopy(lab)
    for y in range(N):
        for x in range(M):
            if sand_box[y][x] == 2:
                Q.append([y, x])

    while Q:
        y, x = Q.popleft()
        for i in range(4):
            dy, dx = y + d[i][0], x + d[i][1]
            if 0 <= dy < N and 0 <= dx < M:
                if sand_box[dy][dx] == 0:
                    sand_box[dy][dx] = 2
                    Q.append([dy, dx])

    global ans
    cnt = 0
    for y in range(N):
        cnt += sand_box[y].count(0)
    ans = max(ans, cnt)

wall(0)
print(ans)