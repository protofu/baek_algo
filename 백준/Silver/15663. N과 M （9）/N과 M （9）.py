import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
num_lst = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    rem = 0
    for i in range(n):
        if not visited[i] and rem != num_lst[i]:
            visited[i] = True
            temp.append(num_lst[i])
            rem = num_lst[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()