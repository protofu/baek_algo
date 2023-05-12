from heapq import heappop, heappush

n, k = map(int, input().split())
heapJ = [list(map(int, input().split())) for _ in range(n)]
heapB = [int(input()) for _ in range(k)]
heapJ.sort()
heapB.sort()
tmp = []
ans = 0
for bag in heapB:
    while heapJ and bag >= heapJ[0][0]:
        heappush(tmp, -heapJ[0][1])
        heappop(heapJ)

    if tmp:
        ans += heappop(tmp)
    elif not heapJ:
        break

print(-ans)