from collections import deque

def bfs(start, goal, maps, col, row):
    # 방명록!
    visit = []
    # 4방향 췤!
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 시작점 방명록 찍고!
    visit.append([start[0], start[1]])
    # 초기값으로 시작
    q = deque([(start[0], start[1], 0)])
    while(q):
        sy, sx, dist = q.popleft()
        # 만약 도착했다면 dist 리턴 때려버리기
        if [sy, sx] == goal:
            return dist
        
        for dy, dx in dir:
            ny, nx = sy+dy, sx+dx
            # 범위, 벽, 왔던길 전부 확인해버리기!
            if 0>ny or 0>nx or col<=ny or row <=nx or maps[ny][nx] == "X" or [ny, nx] in visit: continue
            q.append((ny, nx, dist+1))
            visit.append([ny, nx])
    # 만약 이도저도 못했다면 None을 return 할거임
    return

def solution(maps):
    answer = 0
    start = []
    lever = []
    end = []
    # 가로 세로
    col, row = len(maps), len(maps[0])
    
    # 입구 출구 레버 찾기
    for y in range(col):
        for x in range(row):
            if maps[y][x] == "S":
                start = [y, x]
            elif maps[y][x] == "L":
                lever = [y, x]
            elif maps[y][x] == "E":
                end = [y, x]
                
    # 레버 먼저 찾기!
    go_lever = bfs(start, lever, maps, col, row)
    # 출구 찾기!
    go_end = bfs(lever, end, maps, col, row)
    # 하나라도 None이면 -1
    if go_lever == None or go_end == None:
        answer = -1
    else:
        answer = go_lever+go_end
    
    
    return answer