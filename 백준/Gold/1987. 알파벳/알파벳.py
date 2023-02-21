N, M = map(int, input().split())
box = [list(input()) for _ in range(N)]
y = x = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
stk = []
visited = [0] * 26
cnt = rlt = 1
visited[ord(box[y][x]) - 65] = 1
def dfs(y, x, cnt):
    global rlt
    rlt = max(cnt, rlt)
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if N > ny >= 0 and M > nx >= 0 and not visited[ord(box[ny][nx])-65]:
            visited[ord(box[ny][nx]) - 65] = 1
            dfs(ny, nx, cnt+1)
            visited[ord(box[ny][nx]) - 65] = 0


dfs(0, 0, cnt)
print(rlt)