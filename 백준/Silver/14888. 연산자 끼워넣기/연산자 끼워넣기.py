import sys
from collections import deque
input = sys.stdin.readline

def cal(n, S, p, m, s, h):
    global big, small
    if S == N:
        big = max(big, n)
        small = min(small, n)
        return

    if p > 0:
        cal(n + lst[S], S+1, p-1, m, s, h)
    if m > 0:
        cal(n - lst[S], S+1, p, m-1, s, h)
    if s > 0:
        cal(n * lst[S], S+1, p, m, s-1, h)
    if h > 0:
        cal(int(n / lst[S]), S+1, p, m, s, h-1)

N = int(input())
lst = list(map(int, input().split()))
p, m, s, h = map(int, input().split())
big, small = -1e9, 1e9
cal(lst[0], 1, p, m, s, h)
print(big)
print(small)