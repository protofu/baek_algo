def dfs(sta):
    stack.append(sta)
    visited[sta] = 1
    while stack:
        if not stack:
            return sum(visited)
        else:
            for i in edge[sta]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = 1
            sta = stack.pop()
    return sum(visited)


V = int(input())
E = int(input())
edge = [[] for _ in range(V+1)]
stack = []
visited = [0] * (V+1)
for _ in range(E):
    s, e = map(int, input().split())
    edge[s].append(e)
    edge[e].append(s)

print(dfs(1)-1)