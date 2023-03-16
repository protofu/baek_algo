from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    Q = deque()
    Q.append((A, ""))
    visited = [False] * 10000
    while Q:
        num, path = Q.popleft()
        visited[num] = True
        if num == B:
            print(path)
            break
        num2 = (2*num)%10000
        if not visited[num2]:
            Q.append((num2, path+'D'))
            visited[num2] = True

        num2 = (num-1) % 10000
        if not visited[num2]:
            Q.append((num2, path + 'S'))
            visited[num2] = True

        num2 = (10*num + num//1000) % 10000
        if not visited[num2]:
            Q.append((num2, path + 'L'))
            visited[num2] = True

        num2 = (num//10 +(num%10)*1000) % 10000
        if not visited[num2]:
            Q.append((num2, path + 'R'))
            visited[num2] = True