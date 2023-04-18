import sys
from collections import deque
input = sys.stdin.readline
# 그래프 만들기, 진입차수 기록하기
def Make_Graph():
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
# 위상정렬
def Topology():
    Q = deque()
    for i in range(1, N+1):
        if not in_degree[i]:
            Q.append(i)
            dp[i] = 1
    while Q:
        node = Q.popleft()
        for next in graph[node]:
            in_degree[next] -= 1
            dp[next] = dp[node] + 1
            if not in_degree[next]:
                Q.append(next)

N, K = map(int, input().split())
graph = [[] for _ in range(N+1)] # 그래프
in_degree = [0] * (N+1) # 진입차수 기록
dp = [0] * (N+1)

Make_Graph() # 그래프 만드는 함수
Topology() # 위상정렬
print(*dp[1:])

