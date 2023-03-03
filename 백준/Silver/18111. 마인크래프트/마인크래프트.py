import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = sum([list(map(int, input().split())) for _ in range(N)], [])
end = max(ground)
key = []
time = 256*250000
lend = 0
for g in range(0, end+1):
    dig = fill = now_t = 0
    for i in ground:
        if g > i:
            fill += g - i
        elif g < i:
            dig += i - g
        else:
            pass
    if B < fill-dig:
        pass
    else:
        now_t = dig*2 + fill
        if time >= now_t:
            time = now_t
            lend = g


print(time, lend)