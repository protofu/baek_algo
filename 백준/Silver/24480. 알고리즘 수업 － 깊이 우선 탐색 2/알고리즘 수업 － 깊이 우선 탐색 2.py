import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E, S = map(int, input().strip().split())
node = [[] for _ in range(V+1)]
visited = [0] * (V+1)
rlt =[0] * (V+1)
num = 1
for _ in range(E):
    u, v = map(int, input().strip().split())
    node[u].append(v)
    node[v].append(u)

def dfs(S):
    global num
    visited[S] = 1
    rlt[S] = num
    node[S].sort(reverse=True)
    for i in node[S]:
        if not visited[i]:
            num += 1
            dfs(i)

dfs(S)

for i in rlt[1:]:
        print(i)
    