s = int(input())
swi = [0] + list(map(int, input().split()))
n = int(input())

for _ in range(n):
    per, point = map(int, input().split())
    m = point
    if per == 1:
        swi[point] = int(not swi[point])
        while True:
            point += m
            if point >= len(swi):
                break
            else:
                swi[point] = int(not swi[point])
    else:
        swi[point] = int(not swi[point])
        n = 1
        while True:
            if len(swi) > point+n and point-n > 0 and swi[point-n] == swi[point+n]:
                swi[point - n] = swi[point + n] = int(not swi[point - n])
                n += 1
            else:
                break
swi = swi[1:]
cnt = 0
for i in swi:
    print(i, end=' ')
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0
