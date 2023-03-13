from collections import deque
import sys
input = sys.stdin.readline


N, M =map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(M)]
stk = deque([])
ans = flag = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for y in range(M):
    for x in range(N):
        if tomato[y][x] == 1:
            stk.append([y, x])

def bfs():
    while stk:
        cy, cx = stk.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if M > ny >= 0 and N > nx >= 0 and tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[cy][cx] + 1
                stk.append([ny, nx])
bfs()

for lst in tomato:
    for i in lst:
        if i == 0:
            flag = 1
            break
        if ans < max(lst):
            ans = max(lst)
if flag:
    print(-1)
else:
    if not ans:
        print(0)
    else:
        print(ans-1)
