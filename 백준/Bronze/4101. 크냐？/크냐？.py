while True:
    x, y = map(int, input().split())
    if (x, y) == (0, 0):
        break
    print('Yes' if x>y else 'No')