import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 1e9
party = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            party[i][j] = min(party[i][j], party[i][k]+party[k][j])

for _ in range(M):
    a, b, c = map(int, input().split())
    if c >= party[a-1][b-1]:
        print('Enjoy other party')
    else:
        print('Stay here')
