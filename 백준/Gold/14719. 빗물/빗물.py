H, W = map(int, input().split())
pil = list(map(int, input().split()))
wtr = 0

for i in range(H):
    cnt = 0
    on = 0
    for j in range(W):
        if pil[j]:
            pil[j] -= 1
            wtr += cnt
            cnt = 0
            on = 1
        elif on:
            cnt += 1
print(wtr)