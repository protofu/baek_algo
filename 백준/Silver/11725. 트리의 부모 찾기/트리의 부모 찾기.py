N = int(input())
s_p1 = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    s_p1[v].append(u)
    s_p1[u].append(v)

def bfs(S):
    q = []
    q.append(S)
    visited[S] = S
    while q:
        p = q.pop(0)
        for i in s_p1[p]:
            if not visited[i]:
                visited[i] = p
                q.append(i)
bfs(1)
for i in range(2, N+1):
    print(visited[i])
