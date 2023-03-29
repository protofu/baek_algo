import sys
from collections import deque
input = sys.stdin.readline

def dfs(S, cnt):
    global flag
    if cnt == 4:
        print(1)
        exit()

    for i in graph[S]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N
flag = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
