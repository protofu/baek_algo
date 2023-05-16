m = int(input())
d = int(input())
flag = 0
if m < 2:
    flag = 2
elif m > 2:
    flag = 1
else:
    if d > 18:
        flag = 1
    elif d < 18:
        flag = 2
    else:
        pass

if flag == 0:
    print('Special')
elif flag == 1:
    print('After')
else:
    print('Before')