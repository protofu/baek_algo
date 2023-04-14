INF = int(1e9)
n, m = map(int, input().split())
box = [[INF]*n for _ in range(n)]
for _ in range(m):
    u, v, b = map(int, input().split())
    u, v = u-1, v-1
    if b:
        box[u][v] = box[v][u] = 0
    else:
        box[u][v] = 0
        box[v][u] = 1

ans = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            box[i][j] = min(box[i][j], box[i][k]+box[k][j])
            if i == j:
                box [i][j] = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    print(box[a][b])
