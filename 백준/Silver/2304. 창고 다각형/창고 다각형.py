N = int(input())
lst = []
w = mh = lar = pil = 0
for _ in range(N):
    p, h = list(map(int, input().split()))
    lst += [p, h]
    if p > w:
        w = p
    if mh < h:
        mh = h
store = [0] * (w + 1)

for i in range(1, len(lst), 2):
    store[lst[i-1]] = lst[i]
    pil += lst[i]
for _ in range(mh):
    cnt = 0
    on = 0
    for i in range(w+1):
        if store[i]:
            store[i] -= 1
            lar += cnt
            cnt = 0
            on = 1
        elif on:
            cnt += 1
print(lar+pil)