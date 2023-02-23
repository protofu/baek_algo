import heapq, sys

n = int(input())

H = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(H, (-num, num))
    else:
        if len(H):
            print(heapq.heappop(H)[1])
        else:
            print(0)