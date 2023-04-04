lst = list(map(int, input().split()))
flag = 0
for i in lst:
    if i == 9:
        flag = 1
if flag:
    print('F')
else:
    print('S')