import sys
input = sys.stdin.readline

# 사다리 체크.
def check():
    for i in range(1, N+1):
        tmp = i
        for j in range(1, H+1):
            if ladder[j][tmp] == 1:
                tmp += 1
            elif ladder[j][tmp - 1] == 1:
                tmp -= 1
        if tmp != i:
            return False
    return True

def dfs(cnt, cross_line):
    global ans

    if cross_line >= ans:
        return

    if check():
        ans = cross_line
        return

    for idx in range(cnt+1, len(can_laddering)):
        y, x = can_laddering[idx]
        if ladder[y][x-1] == 0 and ladder[y][x+1] == 0:
            ladder[y][x] = 1
            dfs(idx, cross_line + 1)
            ladder[y][x] = 0

N, M, H = map(int, input().split())
ladder = [[0]*(N+1) for _ in range(H+1)]
ans = 4
can_laddering = []

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1

for i in range(1, H+1):
    for j in range(1, N):
        if not ladder[i][j] and not ladder[i][j-1] and not ladder[i][j+1]:
            can_laddering.append((i, j))

dfs(-1, 0)

if ans < 4:
    print(ans)
else:
    print(-1)