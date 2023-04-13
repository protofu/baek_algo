n, k = map(int, input().split())
box = [[0]*n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    box[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if box[i][k] and box[k][j]:
                box[i][j] = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if box[a][b]:
        print(-1)
    elif box[b][a]:
        print(1)
    else:
        print(0)
