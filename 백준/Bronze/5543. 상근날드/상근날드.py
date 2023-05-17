tmp1 = tmp2 = 2100
for _ in range(3):
    bu = int(input())
    if tmp1 > bu:
        tmp1 = bu
for _ in range(2):
    dr = int(input())
    if tmp2 > dr:
        tmp2 = dr
print(tmp1+tmp2-50)