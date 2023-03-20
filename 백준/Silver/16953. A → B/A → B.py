import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
cnt = flag = 0
while M != N:
    if M%2 and M % 10 == 1:
        M //= 10
    elif M%2 == 0:
        M //= 2
    else:
        flag=1
        break
    cnt += 1
    if M <= 0:
        flag = 1
        break

if flag:
    print(-1)
else:
    print(cnt+1)