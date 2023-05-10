for _ in range(int(input())):
    d, n = map(int, input().split())
    numbers = list(map(lambda x: int(x)%d, input().split()))
    cnt = ans = 0
    cnts = [1] + [0] * (d-1)
    for num in numbers:
        cnt = (cnt + num) % d
        cnts[cnt] += 1
    for x in range(d):
        ans += cnts[x] * (cnts[x] - 1) // 2
    print(ans)