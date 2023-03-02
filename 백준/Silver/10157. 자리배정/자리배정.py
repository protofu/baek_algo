import sys
input = sys.stdin.readline

w, h = map(int, input().split())
seat = [[0]*(w+1) for _ in range(h+1)]
n = int(input())
flag = y = 0
cnt = p = x = 1
if n > w*h:
    print(0)
else:
    w -= 1
    while True:
        for _ in range(h):
            y += p
            seat[y][x] = cnt
            if cnt >= n:
                flag = 1
                break
            cnt += 1
        h -= 1
        if not flag:
            for _ in range(w):
                x += p
                seat[y][x] = cnt
                if cnt >= n:
                    flag = 1
                    break
                else:
                    cnt += 1
        p = -p
        w -= 1
        if flag:
            break
    if y == 0:
        y = 1
    print(x, y)