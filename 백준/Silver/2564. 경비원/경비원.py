w, h = map(int, input().split())
n = int(input())

def go_zero(d, l):
    if d == 1:
        return l
    if d == 2:
        return 2*w+h-l
    if d == 3:
        return 2*w+2*h-l
    if d == 4:
        return w+l

dist = []
posi = [[] for _ in range(5)]
for _ in range(n+1):
    d, l = map(int, input().split())
    dist.append(go_zero(d, l))
ans = 0
for i in range(n):
    short = abs(dist[-1] - dist[i])
    long_l = 2*(w+h) - short
    ans += min(short, long_l)
print(ans)