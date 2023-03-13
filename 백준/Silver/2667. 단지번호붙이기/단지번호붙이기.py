from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(y, x, lst):
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    Q = deque()
    Q.append((y, x))
    lst[y][x] = 0
    cnt = 1
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if N > ny >= 0 and N > nx >= 0:
                if lst[ny][nx]:
                    lst[ny][nx] = 0
                    Q.append((ny, nx))
                    cnt += 1
    return cnt

N = int(input())
lst = [list(map(int, input().strip())) for _ in range(N)]
rlt = []
for y in range(N):
    for x in range(N):
        if lst[y][x]:
            rlt.append(bfs(y, x, lst))

print(len(rlt))
rlt.sort()
for i in rlt:
    print(i)