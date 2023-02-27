L = int(input())
n = int(input())
cake = [0]*(L+1)
cnt = [0]*(n+1)
wanna = lol = 0
for num in range(1, n+1):
    p, k = map(int, input().split())
    for i in range(p, k+1):
        if not cake[i]:
            cake[i] = num
    if k-p+1 > lol:
        lol = k-p+1
        wanna = num
for i in range(1, n+1):
    cnt[i] = cake.count(i)
real = cnt.index(max(cnt))

print(wanna)
print(real)