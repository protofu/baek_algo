import sys
input = sys.stdin.readline
INF = 1e9
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
ans = INF
for s in range(3):
    sel = [[0]*N for _ in range(N)]

    for i in range(3):
        if s != i:
            sel[0][i] = INF
        else:
            sel[0][i] = lst[0][i]

    for i in range(1, N):
        sel[i][0] = min(sel[i-1][1], sel[i-1][2]) + lst[i][0]
        sel[i][1] = min(sel[i-1][2], sel[i-1][0]) + lst[i][1]
        sel[i][2] = min(sel[i-1][0], sel[i-1][1]) + lst[i][2]

    for i in range(3):
        if s != i:
            ans = min(ans, sel[N-1][i])

print(ans)