def dfs(S, tmp, cnt):
    global ans
    if cnt == n:
        ans = min(tmp, ans)
        return

    for e, d in enumerate(box[S]):
        if not visited[e]:
            visited[e] = True
            dfs(e, tmp+d, cnt+1)
            visited[e] = False

INF = int(1e9)
n, s = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
ans = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            box[i][j] = min(box[i][j], box[i][k]+box[k][j])

dfs(s, 0, 0)

print(ans)