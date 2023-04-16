value = 1e10
N = int(input())
x, y = 0, 0
l = 0
r = N - 1

liquid = [int(x) for x in input().split()]
                        
while l < r:
    cur = liquid[l] + liquid[r]

    if abs(cur) <= value:
        y, x, value = liquid[r], liquid[l], abs(cur)

    if cur <= 0:l += 1
    else:r -= 1

print(x, y)

