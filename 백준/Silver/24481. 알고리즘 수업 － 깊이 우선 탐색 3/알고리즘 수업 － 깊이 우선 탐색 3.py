import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
V, E, S = map(int, input().split())
node = [[] for _ in range(V+1)]
visited = [0]*(V+1)
D = 0
dth_lst = [-1] * (V+1)
for _ in range(E):
    u, v = map(int, input().strip().split())
    node[u].append(v)
    node[v].append(u)

def dfs_d(S, D):
    visited[S] = 1
    dth_lst[S] = D
    node[S].sort()
    for i in node[S]:
        if not visited[i]:
            dfs_d(i, D+1)
dfs_d(S, D)
for i in dth_lst[1:]:
    print(i)