lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    w = input()
    cnt = 0
    if w == '#':
        break
    for i in w:
        if i in lst:
            cnt += 1
    print(cnt)