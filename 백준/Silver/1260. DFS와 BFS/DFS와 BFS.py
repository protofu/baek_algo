import sys
input = sys.stdin.readline

V, E, S = map(int, input().split())
node = [[] for _ in range(V+1)]
visited_d = [0] * (V+1)
visited_b = [0] * (V+1)
stk = []
for _ in range(E):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)
for lst in node:
    lst.sort()
n_d = n_b = 1
def dfs(S):
    global n_d
    visited_d[S] = n_d
    print(S, end=' ')
    for i in node[S]:
        if not visited_d[i]:
            n_d += 1
            visited_d[i] = n_d
            dfs(i)
dfs(S)
print()
def bfs(S):
    global n_b
    visited_b[S] = n_b
    stk.append(S)
    print(S, end=' ')
    while stk:
        S = stk.pop(0)
        for i in node[S]:
            if not visited_b[i]:
                n_b += 1
                stk.append(i)
                print(i, end = ' ')
                visited_b[i] = n_b
bfs(S)
