import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
lst = []
def dfs(S):
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in range(1, N+1):
            lst.append(i)
            dfs(i)
            lst.pop()
dfs(1)