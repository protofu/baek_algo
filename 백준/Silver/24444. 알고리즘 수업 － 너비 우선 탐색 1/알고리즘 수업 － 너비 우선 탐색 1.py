import sys
input = sys.stdin.readline

def bfs(S):
    queue.append(S)
    n = 1
    vtd[S] = n
    while queue:
        S = queue.pop(0)
        for i in node[S]:
            if not vtd[i]:
                queue.append(i)
                n += 1
                vtd[i] = n
    for i in range(1, V+1):
        print(vtd[i])


V, E, S = map(int, input().split())
node = [[] for _ in range(V+1)]
queue = []
vtd = [0] * (V+1)
for i in range(E):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)
for i in node:
    i.sort()

bfs(S)
