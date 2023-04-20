import sys
input = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def move(balls):
    next_balls = []
    for ball in balls:
        y, x, m, s, d = ball
        y, x = (y + s * dy[d])%N, (x + s * dx[d])%N
        visited[y][x] += 1
        next_balls.append([y, x, m, s, d])

    return next_balls

def four_move(balls):
    next_balls = []
    for ball in balls:
        y, x, m, s, di = ball
        if visited[y][x] == 1:
            next_balls.append([y, x, m, s, di])
        elif visited[y][x] >= 2:
            if not Map[y][x]:
                Map[y][x] = [m, s, [di]]
            else:
                Map[y][x][0] += m
                Map[y][x][1] += s
                Map[y][x][2].append(di)
    for y in range(N):
        for x in range(N):
            if Map[y][x]:
                m, s, d = Map[y][x]
                _m, s = m//5, s//visited[y][x]
                d = direction(d)
                for dir in d:
                    next_balls.append([y, x, _m, s, dir])
    return next_balls

def direction(dir):
    cnt = 0
    for d in dir:
        if not (d % 2):
            cnt += 1
    if not cnt or cnt == len(dir):
        return [0, 2, 4, 6]
    return [1, 3, 5, 7]

def delete(balls):
    next_balls = []
    for i in range(len(balls)):
        if balls[i][2]:
            next_balls.append(balls[i])
    return next_balls

N, M, K = map(int, input().split())
balls = [list(map(int, input().split())) for _ in range(M)]
ans = 0

for ball in balls:
    ball[0] -= 1
    ball[1] -= 1

for _ in range(K):
    Map = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    balls = move(balls)
    balls = four_move(balls)
    balls = delete(balls)

for ball in balls:
    ans += ball[2]
print(ans)


