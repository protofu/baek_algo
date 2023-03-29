import sys
from collections import deque
input = sys.stdin.readline

def dfs(S):
    global flag

    if S == len(W):
        cnt = 0
        for i in range(len(lst)):
            cnt = max(cnt, int(lst[i]))
        if cnt == len(lst) and not flag:
            print(*lst)
            flag = 1
        return

    if S < len(W) and int(W[S]) <= 50 and not visited[int(W[S])]:
        visited[int(W[S])] = True
        lst.append(W[S])
        dfs(S+1)
        lst.pop()
        visited[int(W[S])] = False

    if S+1 < len(W) and int(W[S:S+2]) <= 50 and not visited[int(W[S:S+2])]:
        visited[int(W[S:S+2])] = True
        lst.append(W[S:S+2])
        dfs(S+2)
        visited[int(W[S:S+2])] = False
        lst.pop()

W = input().rstrip()
flag = 0
lst = deque()
visited = [False]*51
dfs(0)