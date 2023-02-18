import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
def dfs(S):
    lst[S] = -2
    for i in range(V):
        if lst[i] == S:
            dfs(i)

V = int(input())
lst = list(map(int, input().split()))
de = int(input())

dfs(de)

cnt = 0
for i in range(V):
    if lst[i] != -2  and i not in lst:
        cnt += 1
print(cnt)