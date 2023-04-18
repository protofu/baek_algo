from collections import deque

# 그래프 만들기, 진입차수 기록하기
def Make_Graph():
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

# 위상정렬 -> 결과 출력
def Topology():
    Q = deque()
    for i in range(1, N+1):
        if not in_degree[i]:
            Q.append(i)
            dp_time[i] = dev_time[i]
    while Q:
        node = Q.popleft()
        for next in graph[node]:
            in_degree[next] -= 1
            dp_time[next] = max(dp_time[node]+dev_time[next], dp_time[next])
            if not in_degree[next]:
                Q.append(next)


for _ in range(int(input())):
    N, K = map(int, input().split())
    dev_time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)
    dp_time = [0] * (N+1)

    Make_Graph() # 그래프 만드는 함수
    W = int(input())
    Topology() # 위상정렬 과 결과출력
    print(dp_time[W])

