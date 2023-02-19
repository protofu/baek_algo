n = int(input())
stk = [0]
num = 1
rlt = []
flag = 0
for _ in range(n):
    st_n = int(input())
    while num <= st_n:
        stk.append(num)
        num += 1
        rlt.append('+')
    if stk[-1] == st_n:
        stk.pop()
        rlt.append('-')
    else:
        print('NO')
        flag = 1
        break
if not flag:
    for i in rlt:
        print(i)
