import sys
input = sys.stdin.readline

n = int(input())
paper = [[0]*1001 for _ in range(1001)]
for i in range(1, n+1):
    y1, x1, l, h = map(int, input().split())
    for y in range(y1, y1+l):
        paper[y][x1:x1+h] = [i] * h

for i in range(1, n+1):
    large = 0
    for j in paper:
        large += j.count(i)
    print(large)