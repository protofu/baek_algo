import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)


for i in range(M):
    lst = list(map(int, input().split()))
    for s in range(1, lst[0]):
        graph[lst[s]].append(lst[s+1])
        indegree[lst[s+1]] += 1

q = deque()
ans = []
for i in range(1, N+1):
    if not indegree[i]:
        q.append(i)

while q:
    num = q.popleft()
    ans.append(num)
    for i in graph[num]:
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

if len(ans) != N:
    print(0)
else:
    for i in ans:
        print(i)