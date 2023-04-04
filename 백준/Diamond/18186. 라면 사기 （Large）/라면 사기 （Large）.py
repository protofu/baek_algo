fac, B, C = map(int, input().split())
ramen = list(map(int, input().split()))
profit = 0
if B >= C:
    for i in range(fac-2):
        if ramen[i+1] > ramen[i+2]:
            r = min(ramen[i], ramen[i+1]-ramen[i+2])
            profit += r * (B+C)
            ramen[i] -= r
            ramen[i+1] -= r
        if ramen[i] * ramen[i+2] * ramen[i+2]:
            r = min(ramen[i], ramen[i+1])
            profit += r * (B+2*C)
            ramen[i] -= r
            ramen[i+1] -= r
            ramen[i+2] -= r
        if ramen[i]:
            profit += ramen[i] * (B)
            ramen[i] = 0
    if ramen[-1] * ramen[-2]:
        r = min(ramen[-1], ramen[-2])
        profit += r * (B+C)
        ramen[-1] -= r
        ramen[-2] -= r
    if ramen[-2]:
        profit += ramen[-2] * B
        ramen[-2] = 0
    else:
        profit += ramen[-1] * B
        ramen[-1] = 0
else:
    for i in ramen:
        profit += i*B
print(profit)