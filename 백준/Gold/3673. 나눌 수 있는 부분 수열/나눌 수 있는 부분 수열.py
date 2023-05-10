for _ in range(int(input())):
    d, n = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = (s[i - 1] + a[i - 1]) % d
    cnt = [0] * d
    for i in range(n + 1):
        cnt[s[i]] += 1
    ans = 0
    for x in range(d):
        ans += cnt[x] * (cnt[x] - 1) // 2
    print(ans)