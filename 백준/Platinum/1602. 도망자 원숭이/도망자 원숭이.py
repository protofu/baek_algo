import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
INF = 1e9
time = list(map(int, input().split()))
city = [[INF] * N for _ in range(N)]
dog = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    city[a-1][b-1] = city[b-1][a-1] = c
    dog[a-1][b-1] = dog[b-1][a-1] = max(time[a-1], time[b-1])

for k, t in sorted(enumerate(time), key = lambda x: x[1]):
    city[k][k] = 0
    dog[k][k] = t
    for i in range(N):
        for j in range(N):
            if city[i][j] + dog[i][j] > city[i][k] + city[k][j] + max(dog[i][k], dog[k][j]):
                city[i][j] = city[i][k] + city[k][j]
                dog[i][j] = max(dog[i][k], dog[k][j])

for _ in range(Q):
    S, T = map(int, input().split())
    S -= 1
    T -= 1
    if city[S][T] < INF:
        print(city[S][T] + dog[S][T])
    else:
        print(-1)