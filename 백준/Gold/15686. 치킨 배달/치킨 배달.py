import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
Max = ans = 13**13
for y in range(N):
    for x in range(N):
        if box[y][x] == 1:
            home.append([y, x])
        elif box[y][x] == 2:
            chicken.append([y, x])
for i in combinations(chicken, M):
    d = 0
    for j in home:
        chick_home = Max
        for k in i:
            chick_home = min(chick_home, abs(j[0]-k[0])+abs(j[1]-k[1]))
        d += chick_home
    ans = min(d, ans)
print(ans)