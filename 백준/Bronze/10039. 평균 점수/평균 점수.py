SUM = 0
for _ in range(5):
    a = int(input())
    if a <=40:
        SUM += 40
    else:
        SUM += a
print(SUM//5)