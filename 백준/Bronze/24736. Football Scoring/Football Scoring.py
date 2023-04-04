a = [list(map(int, input().split())) for _ in range(2)]

for i in a:
    print(i[0]*6+i[1]*3+i[2]*2+i[3]*1+i[4]*2, end=' ')

