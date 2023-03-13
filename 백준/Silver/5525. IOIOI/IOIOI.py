from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
l = int(input())
S = input()
n = cnt = ans = 0
while n < l-1:
    if S[n:n+3] == 'IOI':
        n += 2
        cnt += 1
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        n += 1
        cnt = 0
print(ans)