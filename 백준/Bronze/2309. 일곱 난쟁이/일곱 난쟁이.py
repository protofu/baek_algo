small = []
for _ in range(9):
    small.append(int(input()))

all = sum(small)
flag = 0
for i in range(9):
    for j in range(i+1,9):
        if all-small[i]-small[j] == 100:
            a, b = small[i], small[j]
            flag = 1
            break
    if flag:
        break
small.sort()
for i in small:
    if i == a or i == b:
        pass
    else:
        print(i)