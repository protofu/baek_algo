import sys
input = sys.stdin.readline

N = int(input())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
ans = 1e9

def dfs(L, idx):
    global ans
    if L == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += box[i][j]
                elif not visited[i] and not visited[j]:
                    link += box[i][j]
        ans = min(ans, abs(start - link))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(L + 1, i + 1)
            visited[i] = False


dfs(0, 0)
print(ans)

