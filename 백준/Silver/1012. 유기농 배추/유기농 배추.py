import sys
sys.setrecursionlimit(10**6)

# 범위 췤!
def is_out(y, x):
    return 0>y or 0>x or col<=y or row <=x
# 4방향 췤!
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def dfs(y, x):
    # 탐색한번 해주고
    for dy, dx in dir:
        ny, nx = y+dy, x+dx
        # 벗어나거나 배추가 아니거나 이미 초토화된 곳이면 넘어갑니다.
        if is_out(ny, nx) or baechu[ny][nx] != 1:
            continue
        # 초토화시 -1로!
        baechu[ny][nx] = -1
        dfs(ny, nx)


for _ in range(int(input())):
    row, col, k = map(int, input().split())
    ans = 0
    # 배추밭 컴온!
    baechu = [[0]*row for _ in range(col)]
    # 배추를 심자!
    for _ in range(k):
        x, y = map(int, input().split())
        baechu[y][x] = 1
    # 배추밭 본격 초토화 작전 시작
    for y in range(col):
        for x in range(row):
            # 배추가 있으면 냠냠
            if baechu[y][x] == 1:
                baechu[y][x] = -1
                dfs(y, x)
                # 한뭉텅이 초토화 성공
                ans+=1
    print(ans)
