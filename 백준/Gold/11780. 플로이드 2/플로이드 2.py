
INF = int(1e9)
n = int(input()) # 도시 수
m = int(input()) # 버스 수
table = [[INF]*(n) for _ in range(n)]
cities = [[()]*(n) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    table[a-1][b-1] = min(table[a-1][b-1], c)
    cities[a-1][b-1] = (a, b)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if table[i][j] > table[i][k]+table[k][j]:
                cities[i][j] = cities[i][k] + cities[k][j][1:]
            table[i][j] = min(table[i][j], table[i][k]+table[k][j])
            table[i][i] = 0

for i in range(n):
    for j in range(n):
        if table[i][j] == INF:
            table[i][j] = 0
        print(table[i][j], end=' ')
    print()

for i in range(n):
    for j in range(n):
        print(len(cities[i][j]), *cities[i][j])
