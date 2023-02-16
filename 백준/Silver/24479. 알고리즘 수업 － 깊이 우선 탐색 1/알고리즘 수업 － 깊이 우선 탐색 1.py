import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E, S = map(int, input().split())
node = [[] for _ in range(V+1)]
num = 1
visited = [0]*(V+1)
for _ in range(E):
    A, B = map(int, input().strip().split())
    node[A].append(B)
    node[B].append(A)

for i in node:
    i.sort()

def dfs(S):
    global num
    visited[S] = num
    for i in node[S]:
        if not visited[i]:
            num += 1
            dfs(i)
dfs(S)
for i in visited[1:]:
    print(i)