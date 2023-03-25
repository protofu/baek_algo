import sys, copy
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
sel = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, len(sel)):
    sel[i][0] = min(sel[i-1][1], sel[i-1][2]) + sel[i][0]
    sel[i][1] = min(sel[i-1][2], sel[i-1][0]) + sel[i][1]
    sel[i][2] = min(sel[i-1][0], sel[i-1][1]) + sel[i][2]

print(min(sel[N-1][0], sel[N-1][1], sel[N-1][2]))