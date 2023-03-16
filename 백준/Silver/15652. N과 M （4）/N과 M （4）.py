import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []

def dfs(S):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(S, N+1):
        lst.append(i)
        dfs(i)
        lst.pop()


dfs(1)