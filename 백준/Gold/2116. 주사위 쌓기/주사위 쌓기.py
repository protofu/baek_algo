n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
Max_ans = 0

for i in range(6):
    s = i
    Max = 0

    for j in range(n):
        if s == 0 or s == 5:
            Max += max(dice[j][1:5])
            if j != n-1 and s == 0:
                s = dice[j+1].index(dice[j][5])
            elif j != n-1 and s == 5:
                s = dice[j + 1].index(dice[j][0])
        elif s == 1 or s == 3:
            Max += max(dice[j][0], dice[j][2], dice[j][4], dice[j][5])
            if j != n-1 and s == 1:
                s = dice[j+1].index(dice[j][3])
            elif j != n-1 and s == 3:
                s = dice[j + 1].index(dice[j][1])

        elif s == 2 or s == 4:
            Max += max(dice[j][0], dice[j][1], dice[j][3], dice[j][5])
            if j != n-1 and s == 2:
                s = dice[j+1].index(dice[j][4])
            elif j != n-1 and s == 4:
                s = dice[j + 1].index(dice[j][2])
    if Max_ans < Max:
        Max_ans = Max
print(Max_ans)