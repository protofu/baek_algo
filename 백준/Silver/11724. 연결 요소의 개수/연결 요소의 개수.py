import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(S):
    visited[S] = True
    for i in node[S]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

V, E = map(int, input().split())
node = [[] for _ in range(V+1)]
visited = [False]*(V+1)
for _ in range(E):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)
cnt = 0
for i in range(1, V+1):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)