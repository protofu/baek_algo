from collections import deque

N, K = map(int, input().split())
visited = [0] * (10**5+1)

def bfs():
    Q = deque()
    Q.append(N)
    while Q:
        S = Q.popleft()
        if S == K:
            print(visited[S])
            break
        lst = [S-1, S+1, S*2]
        for i in lst:
            if 10**5 >= i >= 0 and not visited[i]:
                visited[i] = visited[S] + 1
                Q.append(i)
bfs()
