import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = sorted(list(map(int, input().split())))
visited = [False]*N
lst = []

def dfs():
    if len(lst) == M:
        print(*lst)
        return
    for i in range(N):
        if not visited[i]:
            lst.append(num_lst[i])
            visited[i] = True
            dfs()
            lst.pop()
            visited[i] = False


dfs()