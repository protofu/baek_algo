import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    rlt = [start] * (N + 1)
    Q = [(0, start)]
    while Q:
        a, now = heapq.heappop(Q)
        if a > dist[now]:
            continue

        for next, nextdist in graph[now]:
            cost = nextdist + a
            if cost < dist[next]:
                dist[next], rlt[next] = cost, now
                heapq.heappush(Q, (cost, next))

    tmp = end

    while tmp != start:
        ans.append(str(tmp))
        tmp = rlt[tmp]

    ans.append(str(start))
    ans.reverse()


INF = 1e9
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
dist = [INF for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
ans = []

dijkstra(start)

print(dist[end])
print(len(ans))
print(*ans)