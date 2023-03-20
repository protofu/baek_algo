import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
num_lst = sorted(list(map(int, input().split())))
tmp = []

def dfs(S):
    if len(tmp) == M:
        print(*tmp)
        return
    rem = 0
    for i in range(S, N):
        if rem != num_lst[i]:
            tmp.append(num_lst[i])
            rem = num_lst[i]
            dfs(i)
            tmp.pop()

dfs(0)