n = int(input())
paper = [[0]*1001 for _ in range(1001)]
large = [0]*(n+1)
for i in range(1, n+1):
    y1, x1, l, h = map(int, input().split())
    for y in range(y1, y1+l):
        for x in range(x1, x1+h):
            paper[y][x] = i

for i in range(1, n+1):
    for j in paper:
        large[i] += j.count(i)

for i in range(1, n+1):
    print(large[i])
