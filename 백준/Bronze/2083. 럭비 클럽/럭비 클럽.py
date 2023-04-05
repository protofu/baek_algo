while True:
    a, b, c = input().split()
    if a == '#':
        break
    else:
        if int(b) > 17 or int(c) >= 80:
            print(f'{a} Senior')
        else:
            print(f'{a} Junior')