import heapq, sys

n = int(input())

H = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(H, (abs(num), num)) # 최대값 뽑으려공
    else:
        if len(H):
            print(heapq.heappop(H)[1])
        else:
            print(0)
