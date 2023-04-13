INF = 1e9
for _ in range(int(input())):
    n, k = map(int, input().split())
    box = [[INF]*n for _ in range(n)]

    for _ in range(k):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        box[a][b] = c
        box[b][a] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                box[i][j] = min(box[i][j], box[i][k]+box[k][j])
                if i == j:
                    box[i][j] = 0

    k = int(input())
    friends = list(map(int, input().split()))
    po = 0
    rlt = [0] * n
    for i in friends:
        for j in range(n):
            rlt[j] += box[i-1][j]
    print(rlt.index(min(rlt))+1)
