import heapq

heap = []
n =int(input())

for _ in range(n):
    num = list(map(int, input().split()))
    for i in num:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
print(heap[0])