import sys
sys.setrecursionlimit(10**6)

# 범위 췤!
def is_out(y, x):
    return 0>y or 0>x or h<=y or w<=x
# 8방향 췤!
dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
def dfs(y, x):
    for dy, dx in dir:
        ny, nx = y+dy, x+dx
        # 범위 밖 or 1이 아니라면 넘기기.
        if is_out(ny, nx) or island[ny][nx] != 1: continue
        island[ny][nx] = -1
        dfs(ny, nx)



while(True):
    w, h = map(int, input().split())
    # 탈출조건 넣어주기!
    if (w==0 or h==0): break
    # 웰컴 아일랜드!
    island = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    # 완탐!
    for y in range(h):
        for x in range(w):
            # 콜럼버스 빙의해서 신대륙 발견하기 작전 실행
            if island[y][x] == 1:
                dfs(y, x)
                ans+=1
    print(ans)




