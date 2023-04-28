from collections import deque

# 그래프 만들기, 진입차수 기록하기
def Make_Graph():
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        in_degree[b-1] += 1

# 위상정렬 -> 결과 출력
def Topology():
    Q = deque()
    for i in range(1, N+1):
        if not in_degree[i-1]:
            Q.append(i-1)

    while Q:
        node = Q.popleft()
        rlt.append(node+1)
        for next in graph[node]:
            in_degree[next] -= 1
            if not in_degree[next]:
                Q.append(next)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
in_degree = [0]*N
rlt = []
Make_Graph()
Topology()

print(*rlt)