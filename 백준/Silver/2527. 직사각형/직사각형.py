for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if x1 > x3:
        x1, y1, x2, y2, x3, y3, x4, y4 = x3, y3, x4, y4, x1, y1, x2, y2

    if x2 < x3 or y2 < y3 or y1 > y4: # not match
        print('d')
    elif x2 == x3 and (y2 == y3 or y1 == y4): # dot match
        print('c')
    elif y1 == y4 or x2 == x3 or y2 == y3: # line match
        print('b')
    else:
        print('a')