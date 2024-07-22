from collections import deque


# 범위 췤!
def is_out(y, x, col, row):
    return 0 > y or 0 > x or col <= y or row <= x


# 4방향 췤!
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(y, x, cnt, col, row, land):
    visit = set()
    oil = 0
    q = deque([(y, x)])
    while (q):
        sy, sx = q.popleft()
        # 검은물을 찾을 때마다 +1
        oil += 1
        visit.add((sy, sx))
        # 찾은 포인트는 번호 매겨주기
        land[sy][sx] = cnt
        for dy, dx in dir:
            ny, nx = sy + dy, sx + dx
            if is_out(ny, nx, col, row) or land[ny][nx] != 1 or (ny, nx) in visit: continue
            q.append((ny, nx))
            visit.add((ny, nx))
    # 찾은 검은물 반환
    return oil


def solution(land):
    answer = 0
    # 시추 뽑을 횟수
    row = len(land[0])
    col = len(land)
    oils = {}
    cnt = 2
    # 오일을 찾아서 만수르가 되어보자!
    for y in range(col):
        for x in range(row):
            if land[y][x] == 1:
                # 빌어먹을 함수형 답안지 때문에 그냥 인자로 다 때려박았습니다.
                # 검은물을 딕셔너리 형태로 저장해버리기
                oils[cnt] = bfs(y, x, cnt, col, row, land)
                # 각 포인트마다 매겨줄 번호
                cnt += 1
    oils[0] = 0
    # 전치로 뒤집고
    for col in list(zip(*land)):
        tmp = 0
        # set으로 중복 제거하고
        for row in set(col):
            tmp += oils[row]
        # 크기비교하고
        if answer < tmp:
            answer = tmp
    return answer