import heapq, sys
input = sys.stdin.readline

for tc in range(int(input())):
    num = int(input())
    hq1 = []
    hq2 = []
    visited = [0]*num
    for i in range(num):
        c, n = input().split()
        if c == 'I':
            heapq.heappush(hq1, (int(n), i))
            heapq.heappush(hq2, (-int(n), i))
            visited[i] = True
        else:
            if int(n) == 1:
                while hq2 and not visited[hq2[0][1]]:
                    heapq.heappop(hq2)
                if hq2:
                    visited[hq2[0][1]] = False
                    heapq.heappop(hq2)
            else:
                while hq1 and not visited[hq1[0][1]]:
                    heapq.heappop(hq1)
                if hq1:
                    visited[hq1[0][1]] = False
                    heapq.heappop(hq1)
    while hq1 and not visited[hq1[0][1]]:
        heapq.heappop(hq1)
    while hq2 and not visited[hq2[0][1]]:
        heapq.heappop(hq2)

    if not hq1 or not hq2:
        print("EMPTY")
    else:
        a = -hq2[0][0]
        b = hq1[0][0]
        print("%d %d" % (a, b))