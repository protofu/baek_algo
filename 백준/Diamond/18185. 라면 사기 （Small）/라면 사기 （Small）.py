fac = int(input())
ramen = list(map(int, input().split()))
profit = 0

for i in range(fac-2):
    if ramen[i+1] > ramen[i+2]:
        r = min(ramen[i], ramen[i+1]-ramen[i+2])
        profit += r * 5
        ramen[i] -= r
        ramen[i+1] -= r
    if ramen[i] * ramen[i+2] * ramen[i+2]:
        r = min(ramen[i], ramen[i+1])
        profit += r * 7
        ramen[i] -= r
        ramen[i+1] -= r
        ramen[i+2] -= r
    if ramen[i]:
        profit += ramen[i] * 3
        ramen[i] = 0
if ramen[-1] * ramen[-2]:
    r = min(ramen[-1], ramen[-2])
    profit += r * 5
    ramen[-1] -= r
    ramen[-2] -= r
if ramen[-2]:
    profit += ramen[-2] * 3
    ramen[-2] = 0
else:
    profit += ramen[-1] * 3
    ramen[-1] = 0
print(profit)