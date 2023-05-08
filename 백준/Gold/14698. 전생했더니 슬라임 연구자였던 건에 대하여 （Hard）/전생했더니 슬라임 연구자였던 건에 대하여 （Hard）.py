from heapq import heappop, heappush
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    slime = list(map(int, input().split()))
    ans = 1
    if N!=1:
        heap = []
        for s in slime:
            heappush(heap, s)
        while len(heap)!=1:
            a = heappop(heap)*heappop(heap)
            ans *= a%1000000007
            heappush(heap, a)
    else:
        ans = 1
    print(ans%1000000007)
