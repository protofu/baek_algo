day, gap = map(int, input().split())
days = list(map(int, input().split()))
Max = sum(days[0:gap])
Max_now = sum(days[0:gap])
for i in range(gap, day):
    Max_now = Max_now - days[i-gap] + days[i]
    if Max < Max_now:
        Max = Max_now
print(Max)