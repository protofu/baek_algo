import sys
sys.setrecursionlimit(10**6)

def dfs(S, visit):
    visit.append(S)
    for i in graph[S]:
        if not visited[i]:
            visited[i] = True
            visit.append(i)
            dfs(i, visit)
            visited[i] = False


for _ in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visit1 = []
    visit2 = []
    visited = [False] * (n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[b].append(a)

    son1, son2 = map(int, input().split())
    dfs(son1, visit1)
    dfs(son2, visit2)
    flag = 0
    for i in visit1:
        for j in visit2:
            if i == j:
                print(j)
                flag = 1
                break
        if flag:
            break