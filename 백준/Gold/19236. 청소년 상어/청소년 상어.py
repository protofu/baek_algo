import copy
dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(box, y, x, cnt):
    global eat
    cnt += box[y][x][0]
    eat = max(eat, cnt)
    box[y][x][0] = 0

    # 물고기 MOVE
    for fish in range(1, 17):
        f_y, f_x = -1, -1
        for ny in range(4):
            for nx in range(4):
                if box[ny][nx][0] == fish:
                    f_y, f_x = ny, nx
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = box[f_y][f_x][1]

        for i in range(8):
            nd = (f_d + i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == x and ny == y):
                continue
            box[f_y][f_x][1] = nd
            box[f_y][f_x], box[ny][nx] = box[ny][nx], box[f_y][f_x]
            break

    s_d = box[y][x][1]
    for i in range(1, 5):
        ny, nx = y + dy[s_d] * i, x + dx[s_d] * i
        if (0 <= nx < 4 and 0 <= ny < 4) and box[ny][nx][0] > 0:
            dfs(copy.deepcopy(box), ny, nx, cnt)


box = [[0]*4 for _ in range(4)]

# 맵 만들기
for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    box[i] = [[a1, b1-1], [a2, b2-1], [a3, b3-1], [a4, b4-1]]

eat = 0

dfs(box, 0, 0, 0)
print(eat)
