import sys
from collections import deque

M, N, H = map(int, input().split())

matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

answer = 0

def bfs():
    while Q:
        x,y,z = Q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
                continue

            if matrix[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                Q.append((nx,ny,nz))
                matrix[nx][ny][nz] = matrix[x][y][z] + 1
                visited[nx][ny][nz] = True

Q = deque()
for a in range(H):
    for b in range(N):
        for c in range(M):
            if matrix[a][b][c] == 1 and visited[a][b][c] == 0:
                Q.append((a,b,c))
                visited[a][b][c] = True
bfs()

for a in matrix:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)            
        answer = max(answer, max(b))

print(answer-1)
