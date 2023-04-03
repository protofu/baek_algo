def bfs(start):
    global max_node
    visited = [False] * (n+1)
    Q = [[start, 0]]
    visited[start] = True
    max_dist = 0
    while Q:
        now, now_dist = Q.pop(0)
        for child, child_dist in graph[now]:
            if not visited[child]:
                visited[child] = True
                Q.append([child, now_dist+child_dist])
                if max_dist < now_dist+child_dist:
                    max_dist = now_dist+child_dist
                    max_node = child
    return max_dist

n = int(input())
if n == 1:
    print(0)
else:
    INF = 1e9
    graph = [[] for _ in range(n+1)]
    dist = [INF for _ in range(n-1)]
    max_node = -1
    for _ in range(n-1):
        nodes = list(map(int, input().split()))
        a= len(nodes[1:len(nodes)])
        for i in range(1, a, 2):
            graph[nodes[0]].append([nodes[i], nodes[i+1]])
            graph[nodes[i]].append([nodes[0], nodes[i+1]])


    bfs(1)
    print(bfs(max_node))