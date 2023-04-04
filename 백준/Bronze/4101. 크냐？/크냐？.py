while True:
    a, b = map(int, input().split())
    if a < 1:
        break
    else:
        if a > b:
            print('Yes')
        else:
            print('No')