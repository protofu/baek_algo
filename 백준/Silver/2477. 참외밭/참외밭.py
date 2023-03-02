n = int(input())
l = []
y = x = idx_y = idx_x = 0
sy = sx = 0
for _ in range(6):
    d, long = map(int, input().split())
    l.append([d, long])
for i in range(6):
    if l[i][0] == 1 or l[i][0] == 2: # 가로
        if l[i][1] > y:
            y = l[i][1]
            idx_y = i
    elif l[i][0] == 3 or l[i][0] == 4: # 세로
        if l[i][1] > x:
            x = l[i][1]
            idx_x = i
sy = abs(l[(idx_y-1)%6][1] - l[(idx_y+1)%6][1])
sx = abs(l[(idx_x-1)%6][1] - l[(idx_x+1)%6][1])
print((y*x-sy*sx)*n)
