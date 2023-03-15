import sys
input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
Max = max(map(max, box))
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

def dfs(y, x, cnt, four):
    global ans
    if four + Max * (4 - cnt) <= ans:
        return
    if cnt == 4:
        ans = max(ans, four)
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if N > ny >= 0 and M > nx >= 0 and not visited[ny][nx]:
            if cnt == 2:
                visited[ny][nx] = True
                dfs(y, x, cnt+1, four+box[ny][nx])
                visited[ny][nx] = False
            visited[ny][nx] = True
            dfs(ny, nx, cnt+1, four+box[ny][nx])
            visited[ny][nx] = False

for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(y, x, 1, box[y][x])
        visited[y][x] = False

print(ans)