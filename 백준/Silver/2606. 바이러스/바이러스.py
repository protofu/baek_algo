V = int(input())
E = int(input())
node = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for _ in range(E):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

def bfs(S):
    Q = []
    Q.append(S)
    while Q:
        S = Q.pop(0)
        for i in node[S]:
            if not visited[i]:
                visited[i] = 1
                Q.append(i)
    return sum(visited)-1

print(bfs(1))