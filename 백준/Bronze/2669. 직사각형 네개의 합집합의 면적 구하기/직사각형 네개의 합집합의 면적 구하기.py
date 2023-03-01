paper = [[0] * 101 for _ in range(101)]
Sum = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        paper[y][x1:x2] = [1]*(x2-x1)

for i in paper:
    Sum += sum(i)

print(Sum)