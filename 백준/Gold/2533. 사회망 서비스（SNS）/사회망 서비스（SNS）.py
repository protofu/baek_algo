import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(son, parent):
    visited[son] = True

    for i in graph[son]:
        if not visited[i]:
            dfs(i ,son)

    if parent and not EA[son]:
        EA[parent] = True

N = int(input())
graph = [[] for _ in range(N+1)]
EA = [False] * (N+1)
visited = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    # a, b = a-1, b-1
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

print(EA.count(True))
