from collections import deque

def bfs(maps):
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    col, row = len(maps), len(maps[0])
    q = deque([(0, 0, 1)])
    visit = set((0, 0))
    while(q):
        sy, sx, cnt = q.popleft()
        # 도착하면 depth 반환
        if (sy, sx) == (col-1, row-1):
            return cnt
        for dy, dx in dir:
            ny, nx = sy+dy, sx+dx
            # 범위 췤! 길 췤!
            if 0<=ny<col and 0<=nx<row and maps[ny][nx] == 1 and (ny, nx) not in visit:
                q.append((ny, nx, cnt+1))
                # 방문점 음수로
                visit.add((ny, nx))
    return -1
def solution(maps):
    return bfs(maps)