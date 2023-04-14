INF = int(1e9)
N, M = map(int, input().split())
box = [[INF]*N for _ in range(N)]
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    box[a][b] = min(box[a][b], c)
    box[b][a] = min(box[b][a], c)
    edges.append((a, b, c))

ans = INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            box[i][j] = min(box[i][j], box[i][k]+box[k][j])
            if i == j:
                box[i][j] = 0

for i in range(N):
    temp = 0
    for j in range(M):
        temp = max(temp, box[i][edges[j][0]] + box[i][edges[j][1]] + edges[j][2])
    ans = min(ans, temp)
print(ans/2)