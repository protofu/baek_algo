t = int(input())

box = [[0 for _ in range(100)] for _ in range(100)]
xy_lst = []
area = 0
for i in range(t):
    xy_lst.append(list(map(int, input().split())))

for i in xy_lst:
    for j in range(i[1], i[1]+10):
            for k in range(i[0], i[0]+10):
                box[j][k] = 1
for i in box:
    area += sum(i)
print(area)