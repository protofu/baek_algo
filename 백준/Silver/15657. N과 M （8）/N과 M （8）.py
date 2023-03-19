import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
num_lst = sorted(list(map(int, input().split())))
lst = []
def dfs(S):
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in range(S, N):
            lst.append(num_lst[i])
            dfs(i)
            lst.pop()
dfs(0)