dy, dx = [1, 1, 0], [0, 1, 1]

def check(y, x, cnt):
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return
    if x >= 10:
        check(y+1, 0, cnt)
        return

    if paper[y][x]:
        for i in range(5):
            if visited[i] == 5:
                continue
            if y+i >= 10 or x+i >= 10:
                continue

            flag = True
            for j in range(y, y+i+1):
                for k in range(x, x+i+1):
                    if not paper[j][k]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                for j in range(y, y+i+1):
                    for k in range(x, x+i+1):
                        paper[j][k] = 0
                visited[i] += 1
                check(y, x+i+1, cnt+1)
                visited[i] -= 1
                for j in range(y, y+i+1):
                    for k in range(x, x+i+1):
                        paper[j][k] = 1
    else:
        check(y, x+1, cnt)


paper = [list(map(int, input().split())) for _ in range(10)]
visited = [0]*5
ans = 26
check(0, 0, 0)

print(ans if ans != 26 else -1)