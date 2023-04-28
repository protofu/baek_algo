dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]


N, M, K = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(N)]
dirs = list(map(int, input().split()))
smell = [[[0, 0]]*N for _ in range(N)]
pri = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]


def smellRest():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if shark[i][j] != 0:
                smell[i][j] = [shark[i][j], K]


def move():
    sand = [[0] *N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if shark[x][y] != 0:
                dir = dirs[shark[x][y] - 1]
                find = False
                for idx in pri[shark[x][y] - 1][dir - 1]:
                    ny, nx = y + dy[idx - 1], x + dx[idx - 1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][1] == 0:
                            dirs[shark[x][y] - 1] = idx
                            if sand[nx][ny] == 0:
                                sand[nx][ny] = shark[x][y]
                            else :
                                sand[nx][ny] = min(shark[x][y], sand[nx][ny])
                            find = True
                            break
                if find:
                    continue
                for idx in pri[shark[x][y] - 1][dir - 1]:
                    ny, nx = y + dy[idx - 1], x + dx[idx - 1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][0] == shark[x][y]:
                            dirs[shark[x][y] - 1] = idx
                            sand[nx][ny] = shark[x][y]
                            break
    return sand

ans = 0

while True:
    smellRest()
    sand = move()
    shark = sand
    ans += 1
    flag = True
    for y in range(N):
        for x in range(N):
            if shark[y][x]>1:
                flag = False
    if flag:
        print(ans)
        break
    if ans >= 1000:
        print(-1)
        break