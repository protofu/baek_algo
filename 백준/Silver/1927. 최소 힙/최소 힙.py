import heapq as h
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x:
        h.heappush(heap, x)
    elif x == 0 and heap:
        print(h.heappop(heap))
    else:
        print(0)