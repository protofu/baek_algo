INF = int(1e9)
n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
ans = 0

for k in range(n):
    for i in range(n):
        if i != k:
            for j in range(n):
                if i != j and k != j:
                    if box[i][j] == box[i][k]+box[k][j]:
                        visited[i][j] = True
                    elif box[i][j] > box[i][k]+box[k][j]:
                        ans = -1
if not ans:
    for i in range(n):
        for j in range(i, n):
            if not visited[i][j]:
                ans += box[i][j]
print(ans)
