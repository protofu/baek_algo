def bfs(start):
    dist[start] = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            for n, t in graph[j]:
                if dist[n] > dist[j] + t:
                    dist[n] = dist[j] + t
                    if i == N:
                        return True


for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dist = [1e9 for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append([E, T])
        graph[E].append([S, T])
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append([E, -T])

    flag = bfs(1)
    if not flag:
        print('NO')
    else:
        print('YES')